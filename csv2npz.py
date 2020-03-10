import pandas as pd
import numpy as np
import sys

def set_control(df_s):
    dt=df_s[['torch_left','torch_right']].values
    dt=dt.astype(np.float32)
    for i in range(48,-1,-1):
        dt[i]=dt[i+1]-0.02
    dt[dt<0]=0
    return(dt)

args = sys.argv
arg1=args[1]
arg2=args[2]
arg3=args[3]

df=pd.read_csv(arg1)
for index,row in df.iterrows():
    fname=row['children_csv_name']
    df_s=pd.read_csv(arg2+'/'+fname)
    dt=set_control(df_s)
    np_name=fname.split('.')[0]
    print(np_name)
    np.savez_compressed(arg3+'/'+np_name+'.npz',dt)

