"""Run python official_aps.py path/to/uci-421.zip from this directory."""
import sys, hashlib, zipfile, io, math
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import binom,beta
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
with zipfile.ZipFile(sys.argv[1]) as z:
 def load(key):
  raw=z.read('aps_failure_'+key+'_set.csv')
  print(key,hashlib.sha256(raw).hexdigest(),flush=True)
  d=pd.read_csv(io.BytesIO(raw[raw.index(b'class,aa_000'):]),na_values='na')
  labels=d.pop('class')
  assert set(labels)=={'pos','neg'}
  return d,(labels=='pos').to_numpy(dtype=int)
 X,y=load('training');T,v=load('test')
assert (len(y),sum(y),len(v),sum(v))==(60000,1000,16000,375) and list(X)==list(T) and X.shape[1]==170
fit,cal=train_test_split(np.arange(len(y)),test_size=.25,stratify=y,random_state=42)
rows=[];scores=[]
for name,est in [('LR',make_pipeline(SimpleImputer(strategy='median'),StandardScaler(),LogisticRegression(max_iter=3000))),('RF',make_pipeline(SimpleImputer(strategy='median'),RandomForestClassifier(n_estimators=200,min_samples_leaf=2,random_state=42,n_jobs=6)))]:
 est.fit(X.iloc[fit],y[fit]); c=est.predict_proba(X.iloc[cal])[:,1];s=est.predict_proba(T)[:,1]
 for split,idx,truth,pred in [('cal',cal,y[cal],c),('test',np.arange(len(v)),v,s)]:
  scores.append(pd.DataFrame(dict(model=name,split=split,row=idx,label=truth,score=pred)))
 faults=np.sort(c[y[cal]==1]);m=len(faults)
 p,r,z=precision_recall_curve(y[cal],c);f=5*p[:-1]*r[:-1]/np.maximum(4*p[:-1]+r[:-1],1e-15)
 rules={'Default':.5,'F2':z[np.flatnonzero(f==max(f))[-1]],'Emp80':faults[m-math.ceil(.8*m)]}
 for recall in [.8,.9]:
  ranks=np.arange(1,m+1);rules[f'R{int(100*recall)}']=faults[ranks[binom.sf(ranks-1,m,1-recall)>=.95][-1]-1]
 for rule,threshold in dict(rules,Top5=np.nan).items():
  flag=s>=threshold
  if rule=='Top5':flag[np.argsort(-s,kind='stable')[:len(s)//20]]=True
  tp=sum(v[flag]);a=sum(flag);P=sum(v)
  rows.append(dict(model=name,rule=rule,threshold=threshold,alerts=a,tp=tp,fp=a-tp,fn=P-tp,recall=tp/P,per1000=1000*a/len(s),recall_lo=beta.ppf(.025,tp,P-tp+1) if tp else 0,recall_hi=beta.ppf(.975,tp+1,P-tp) if tp<P else 1))
pd.concat(scores).to_csv('official_scores.csv.gz',index=False)
out=pd.DataFrame(rows);out.to_csv('official_results.csv',index=False);print(out.to_string(index=False))
