from pathlib import Path
import math
import pandas as pd
import numpy as np
from scipy.stats import binom
from sklearn.metrics import precision_recall_curve,average_precision_score
rows=[]
for file in sorted(Path('scores').glob('*.gz')):
 name,seed=file.name.split('.')[0].split('_')
 for model,g in pd.read_csv(file,float_precision='round_trip').groupby('model'):
  c=g[g.split=='cal'];t=g[g.split=='test'];assert not set(c.row)&set(t.row)
  s=t.score.to_numpy();y=t.label.to_numpy();n=len(y);P=y.sum();fault=np.sort(c.loc[c.label==1,'score']);m=len(fault)
  p,r,z=precision_recall_curve(c.label,c.score);f=5*p[:-1]*r[:-1]/np.maximum(4*p[:-1]+r[:-1],1e-15)
  rules={'Default':.5,'F2':z[np.flatnonzero(f==max(f))[-1]],'Emp80':fault[m-math.ceil(.8*m)]}
  for recall in (.8,.9):
   ranks=np.arange(1,m+1);valid=ranks[binom.sf(ranks-1,m,1-recall)>=.95];rules[f'R{int(100*recall)}']=fault[valid[-1]-1] if len(valid) else -np.inf
  for rule,th in dict(rules,**{f'Top{i}':None for i in [1,2,5,10,20,30,40]}).items():
   flag=np.zeros(n,bool)
   if th is None:flag[np.argsort(-s,kind='stable')[:int(rule[3:])*n//100]]=True
   else:flag=s>=th
   a=flag.sum();tp=y[flag].sum()
   rows.append(dict(dataset=name,seed=int(seed),model=model,rule=rule,threshold=th,N=n,P=P,m=m,alerts=a,tp=tp,fp=a-tp,fn=P-tp,recall=tp/P,workload=1000*a/n,precision=tp/a if a else 0,ap=average_precision_score(y,s),floor80=math.ceil(.8*P),cap5=n//20))
d=pd.DataFrame(rows);assert len(d)==1680
d['hit']=d.recall>=.8;d['joint']=d.hit&(d.alerts<=d.cap5)
assert (d.tp<=d.alerts).all()
d.to_csv('expanded_results.csv',index=False)
print(d.query('model=="RF" and rule in ["Top5","R80","Emp80","F2"]').groupby(['dataset','rule']).agg({'recall':'median','workload':'median','hit':'sum','joint':'sum'}).round(3))
