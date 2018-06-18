#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:04:39 2018

@author: leandro
"""
import pandas as pd 

path = '/media/leandro/BKP/Documentos/IC/Tempo-Clima/Dados/EMA/Unidos_v2/by_region/'
files = ['NORTE.csv','CENTRO_OESTE.csv','SUL.csv','SULDESTE.csv','NORDESTE.csv']

for table in files:
    df_temp = pd.read_csv(str(path+table))
    
    for i in range(1,12):
        df_month = df_temp.loc[lambda df: df.Month == 1, :]
        df_temp = df_temp.drop(df_month.index)
        df_month.to_csv(str('/media/leandro/BKP/Documentos/IC/Tempo-Clima/Dados/EMA/Unidos_v2/by_region/' + table + str(i) + '.csv'))
        del df_month
        print(str(table+str(i)))
        
        