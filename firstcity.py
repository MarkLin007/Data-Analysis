# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:07:28 2017

@author: Administrator
"""

import pandas as pd
df=pd.read_excel(r'C:\Users\Administrator\Desktop\test.xlsx')

def group_max_data(x):
    raw=df[df['日期']==x] #按日期划分数据集
    j_max=raw['数值'].max() #计算每个数据集的数值最大值
    d_max=raw[raw['数值']==j_max] #筛选每个数据集的数值最大值所在行
    return d_max 

if __name__=='__main__':
    listf=[]
    for x in list(df['日期'].unique()):
        listout=list(group_max_data(x).index)#计算每个数据集的数值最大值索引号
        for y in listout:
            listf.append(y)
    outdata=df[df.index.isin(listf)].sort_values(by='日期')
    ljidata=outdata.groupby(outdata['城市']).count().drop('日期',axis=1)
    print('每天最大值所在城市-----------------')
    print(outdata)
    print('累计最大值所在城市-----------------')
    print(ljidata[ljidata['数值']==ljidata['数值'].max()])