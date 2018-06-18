# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:36:01 2018

@author: leonoro
"""
import pandas as pd

path = '/home/leonoro/Documents/Leandro/by_region/'
files = ['SUL.csv','SULDESTE.csv','NORTE.csv','NORDESTE.csv','CENTRO_OESTE.csv']

for table in files:
    df_temp = pd.read_csv(str(path+table))
    df_temp = df_temp.drop(columns = ['Unnamed: 0'])
    for i in range(1,13):
        df_month = df_temp.loc[lambda df: df.Month==i,:]
        df_temp = df_temp.drop(df_month.index)
        df_month.to_csv(str(path+'by_month/'+ table[:len(table)-4] +'_'+str(i)+'.csv'))
        del df_month
        print(table+''+str(i))
