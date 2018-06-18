# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
from os import walk
import pandas as pd

if "__init__":
## Criando os dataframes 
    
    errors = open('./nao-encontrado.txt','a')
    for (dirpath, dirnames, filenames) in walk('./Dados/EMA/Unidos'):
       # print(dirpath)        
       # print(dirnames)
        if filenames !=[] and dirpath.find('v2')==-1:
            filenames.sort()
            i = 0
            while(i<len(filenames)):
                    data = pd.read_csv(str(dirpath+'/'+filenames[i]))
                    df_no_zero = data.drop(data.loc[data['H(UTC)']==0].index).reset_index(drop=True)
                    df_zero = data.loc[data['H(UTC)']==0].drop_duplicates(subset=['Year','Month','Day']).reset_index(drop=True)
                    df_no_zero = df_no_zero.append(df_zero).sort_values(by=['Year','Month','Day','H(UTC)'])
                    df_no_zero.to_csv(str(dirpath +'/v2/'+filenames[i]+ '_v2.csv'))     
                    print(filenames[i])
                    i+=1        
            print(dirpath)
    errors.close()