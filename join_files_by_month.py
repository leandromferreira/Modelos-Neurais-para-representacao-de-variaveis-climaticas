#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 07:32:33 2018

@author: leandro
"""

import pandas as pd

path = '/media/leandro/BKP/Documentos/IC/Tempo-Clima/Dados/EMA/Unidos_v2/by_month/'
regs = ['NORTE','CENTRO_OESTE','SUL','SULDESTE','NORDESTE']

for i in range (1,13):
    df_month = pd.DataFrame(columns = ['Year', 'Month', 'Day', 'H(UTC)', 'PRECIPITACAO (mm)',
                                               'PRESSAO ATMOSFERICA (hPa)', 'PRESSAO ATMOSFÉRICA MAXIMA (hPa)',
                                               'PRESSAO ATMOSFÉRICA MINIMA (hPa)', 'RADIACAO GLOBAL (KJ/M2)',
                                               'TEMPERATURA DO AR (C)', 'TEMPERATURA DO PONTO DE ORVALHO (C)',
                                               'TEMPERATURA MAXIMA (C)', 'TEMPERATURA MINIMA (C)',
                                               'TEMPERATURA MÁXIMA DO PONTO DE ORVALHO (C)',
                                               'TEMPERATURA MÍNIMA DO PONTO DE ORVALHO (C)',
                                               'UMIDADE RELATIVA DO AR (%)', 'UMIDADE RELATIVA DO MAXIMA AR (%)',
                                               'UMIDADE RELATIVA DO MINIMA AR (%)', 'VENTO VELOCIDADE ',
                                               'VENTO, DIRECAO (graus)', 'VENTO, RAJADA MAXIMA (m/s)', 'Latitude',
                                               'Longitude', 'Altitude(metros)', 'Nome', 'Codigo OMM']
                                )
    df_month = pd.read_csv(str(path+regs[0]+'_'+str(i)+'.csv'))
        
    for reg in regs[1:]:
        df_month = df_month.append(pd.read_csv(str(path+reg+'_'+str(i)+'.csv')))
    df_month.to_csv(str(path + 'Brasil_' + str( i ) + '.csv' ) )
    del df_month
    print(i)