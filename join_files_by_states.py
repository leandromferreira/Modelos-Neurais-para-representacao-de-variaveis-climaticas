#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:11:56 2018

@author: leandro
"""

from os import walk
import pandas as pd

if "__init__":
## Criando os dataframes 
    path= './Dados/EMA/Unidos_v2'
    errors = open('./nao-encontrado.txt','a')
    for (dirpath, dirnames, filenames) in walk(path):
       # print(dirpath)        
       # print(dirnames)
        if filenames !=[] and dirpath.find('states')==-1:
            filenames.sort()
            i = 0
            df_state = pd.DataFrame(columns = ['Year', 'Month', 'Day', 'H(UTC)', 'PRECIPITACAO (mm)',
                                               'PRESSAO ATMOSFERICA (hPa)', 'PRESSAO ATMOSFÉRICA MAXIMA (hPa)',
                                               'PRESSAO ATMOSFÉRICA MINIMA (hPa)', 'RADIACAO GLOBAL (KJ/M2)',
                                               'TEMPERATURA DO AR (C)', 'TEMPERATURA DO PONTO DE ORVALHO (C)',
                                               'TEMPERATURA MAXIMA (C)', 'TEMPERATURA MINIMA (C)',
                                               'TEMPERATURA MÁXIMA DO PONTO DE ORVALHO (C)',
                                               'TEMPERATURA MÍNIMA DO PONTO DE ORVALHO (C)',
                                               'UMIDADE RELATIVA DO AR (%)', 'UMIDADE RELATIVA DO MAXIMA AR (%)',
                                               'UMIDADE RELATIVA DO MINIMA AR (%)', 'VENTO VELOCIDADE ',
                                               'VENTO, DIRECAO (graus)', 'VENTO, RAJADA MAXIMA (m/s)', 'Latitude',
                                               'Longitude', 'Altitude(metros)', 'Nome', 'Codigo OMM'])
            while(i<len(filenames)):
                    data = pd.read_csv(str(dirpath+'/'+filenames[i]))
                    df_state = df_state.append(data)
                    print(filenames[i])
                    i+=1        
            print(dirpath)
            df_state.to_csv(str(path + '/states/'+dirpath.split('/')[5]+'.csv'))
    errors.close()