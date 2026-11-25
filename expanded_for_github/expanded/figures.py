import pandas as pd,numpy as np,matplotlib.pyplot as plt
d=pd.read_csv('expanded_results.csv')
names=['APS','AI4I','Conveyor','Bogie','Sensor','Machines','Helicopter']
fig,axes=plt.subplots(2,4,figsize=(11,5.6),sharex=True,sharey=True)
for ax,n in zip(axes.flat,names):
 for model,sty in [('LR','--'),('RF','-')]:
  vals=d[(d.dataset==n)&(d.model==model)&d.rule.str.startswith('Top')].copy()
  vals['budget']=vals.rule.str[3:].astype(int)
  t=vals.groupby('budget').recall.agg(['median','min','max'])
  ax.plot(t.index,t['median']*100,sty,label=model);ax.fill_between(t.index,t['min']*100,t['max']*100,alpha=.1)
 ax.set_title(n);ax.axhline(80,color='gray',lw=.7);ax.axvline(5,color='gray',lw=.7)
axes.flat[-1].axis('off');axes.flat[0].legend();fig.supxlabel('Inspection budget (% of records)');fig.supylabel('Fault recall (%)');fig.tight_layout();fig.savefig('budget.png',dpi=300);plt.close(fig)
fig,ax=plt.subplots(figsize=(9,3.8));y=np.arange(7)
for i,rule in enumerate(['Emp80','R80','R90']):
 v=d.query('model=="RF" and rule==@rule').groupby('dataset').workload.agg(['median','min','max']).loc[names]
 ax.errorbar(v['median'],y+(i-1)*.19,xerr=[v['median']-v['min'],v['max']-v['median']],fmt=['o','s','^'][i],label=rule,capsize=2)
ax.set_yticks(y,names);ax.invert_yaxis();ax.set_xlabel('Inspections per 1,000 records (median and observed range)');ax.legend();fig.tight_layout();fig.savefig('uncertainty.png',dpi=300)
