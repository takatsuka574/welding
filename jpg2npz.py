import pandas as pd
import make_polar
import cv2
import numpy as np
import sys

args = sys.argv
if(len(args)<3):
    exit()
arg1=args[1]
arg2=args[2]
arg3=args[3]

print(arg1,arg2,arg3)
if(len(args)==4):
    df1=pd.read_csv(arg1+"/master_file.csv")
else:
    df1=pd.read_csv(arg1+"/master_test.csv")
df2=pd.read_pickle(arg1+"/ImgList.pcl")
p_dict=df2.to_dict(orient="index")

np_low=np.zeros((50,200,500))
np_high=np.zeros((50,200,500))
for index1, row1 in df1.iterrows():
    csv_name=row1[0]
    print(csv_name)
    df3=pd.read_csv(arg1+"/csvdata/"+csv_name)
    x0=row1["x_electrode"]
    y0=row1["y_electrode"]
    for index2, row2 in df3.iterrows():
        f_high=row2["fig_high"]
        f_low=row2["fig_low"]
        p_high=p_dict[f_high]['PATH']
        p_low=p_dict[f_low]['PATH']
        
        if(p_high[:-3]!="jpg"):
            p_high=p_high+"/"+f_high
        if(p_low[:-3]!="jpg"):
            p_low=p_low+"/"+f_low
            
        x=row2["x_electrode"]
        y=row2["y_electrode"]

        if(x==0):
            x=x0
            y=y0
        jpg1=cv2.imread(arg2+"/"+p_high, cv2.IMREAD_GRAYSCALE)
        jpg2=cv2.imread(arg2+"/"+p_low, cv2.IMREAD_GRAYSCALE)
        pimg1=make_polar.to_polar(jpg1,y,x,500)
        pimg2=make_polar.to_polar(jpg2,y,x,500)
        np_high[index2]=pimg1
        np_low[index2]=pimg2
    np_name=csv_name.split('.')[0]
    np.savez_compressed(arg3+"/"+np_name+'.npz', np_high, np_low)



