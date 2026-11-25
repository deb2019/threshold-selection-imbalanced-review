"""Generate scores for the seven prepared CSV files (place them in data/)."""
import sys
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split,GroupShuffleSplit
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
specs={
'APS':('aps_failure_reduced_30k','class',[]),
'AI4I':('ai4i2020_preprocessed','Machine failure',['TWF','HDF','PWF','OSF','RNF']),
'Conveyor':('pre_conveyor_fault','Fault',[]),
'Bogie':('pre_train_fault','condition',['label']),
'Sensor':('pre_pm_sensor_imb','fail',[]),
'Machines':('preprocessed_maintenance_data','Failures',['Machine_ID','Downtime','Remaining_Useful_Life']),
'Helicopter':('Helicopter_Anomaly_dataset','Lavel',[])}
def run(name):
 file,target,drop=specs[name]
 df=pd.read_csv('data/'+file+'.csv').drop_duplicates().reset_index(drop=True);y=df[target].to_numpy();X=df.drop(columns=[target]+drop)
 for seed in range(42,52):
  if name=='Machines':
   groups=df.Machine_ID
   tr,h=next(GroupShuffleSplit(n_splits=1,test_size=.4,random_state=seed).split(X,y,groups))
   c,t=next(GroupShuffleSplit(n_splits=1,test_size=.5,random_state=seed+1).split(X.iloc[h],y[h],groups.iloc[h]))
   cal,test=h[c],h[t]
  else:
   tr,h=train_test_split(np.arange(len(y)),test_size=.4,stratify=y,random_state=seed)
   cal,test=train_test_split(h,test_size=.5,stratify=y[h],random_state=seed+1)
  data=[]
  for key,model in [('LR',make_pipeline(SimpleImputer(strategy='median'),StandardScaler(),LogisticRegression(max_iter=3000))),('RF',make_pipeline(SimpleImputer(strategy='median'),RandomForestClassifier(n_estimators=200,min_samples_leaf=2,random_state=42,n_jobs=2)))]:
   model.fit(X.iloc[tr],y[tr])
   for part,idx in [('cal',cal),('test',test)]:
    data.append(pd.DataFrame(dict(dataset=name,model=key,split=part,row=idx,label=y[idx],score=model.predict_proba(X.iloc[idx])[:,1])))
  pd.concat(data).to_csv(f'scores/{name}_{seed}.csv.gz',index=False)
if __name__=='__main__':
 Path('scores').mkdir(exist_ok=True)
 for name in sys.argv[1:] or specs:run(name)
