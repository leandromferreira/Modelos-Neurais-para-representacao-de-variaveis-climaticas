# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
from os import walk
import pandas as pd
from unicodedata import normalize

## Rename das colunas das 0 hora para faciliar na atribuição futura

def change_name_columns(tablePath,table2Path):                   # Tabela1
    
    table = pd.read_excel(tablePath,skiprows=[0,1,2,3,4,5,6,7],header=1)
    columns = []    
    for col in table.columns.unique():
        columns.append(normalize('NFKD',col).encode('ASCII','ignore').decode('ASCII').replace('   ',' '))
    table.columns = columns
    table2 = pd.read_excel(table2Path,skiprows=[0,1,2,3,4,5,6,7],header=1)  
    columns = []    
    for col in table2.columns:
        if col.find('VENTO VELOCIDADE (m/s)')!=-1:
            col = col.replace('VENTO VELOCIDADE (m/s)','VENTO VELOCIDADE ')
        columns.append(normalize('NFKD',col).encode('ASCII','ignore').decode('ASCII').replace('   ',' '))
    table2.columns = columns
    
    table = table.rename(index=str,columns={'TEMPERATURA DO AR (C)':'TEMPERATURA DO AR (C).0',
                                    'TEMPERATURA MAXIMA (C)':'TEMPERATURA MAXIMA (C).0',
                                    'TEMPERATURA MINIMA (C)':'TEMPERATURA MINIMA (C).0',
                                    'TEMPERATURA MAXIMA (C)':'TEMPERATURA MAXIMA (C).0',
                                    'TEMPERATURA MINIMA (C)':'TEMPERATURA MINIMA (C).0',
                                    'UMIDADE RELATIVA DO AR (%)':'UMIDADE RELATIVA DO AR (%).0',
                                    'UMIDADE RELATIVA MAXIMA DO AR (%)': 'UMIDADE RELATIVA MAXIMA DO AR (%).0',
                                    'UMIDADE RELATIVA MINIMA DO AR (%)':'UMIDADE RELATIVA MINIMA DO AR (%).0',
                                    'TEMPERATURA DO PONTO DE ORVALHO (C)':'TEMPERATURA DO PONTO DE ORVALHO (C).0',
                                    'TEMPERATURA MINIMA DO PONTO DE ORVALHO (C)':'TEMPERATURA MINIMA DO PONTO DE ORVALHO (C).0',
                                    'TEMPERATURA MAXIMA DO PONTO DE ORVALHO (C)':'TEMPERATURA MAXIMA DO PONTO DE ORVALHO (C).0'})
    
    table2 = table2.rename(index=str,columns={'PRESSAO ATMOSFERICA (hPa)':'PRESSAO ATMOSFERICA (hPa).0',
                                    'PRESSAO ATMOSFERICA MAXIMA (hPa)':'PRESSAO ATMOSFERICA MAXIMA (hPa).0',
                                    'PRESSAO ATMOSFERICA MINIMA (hPa)':'PRESSAO ATMOSFERICA MINIMA (hPa).0',
                                    'VENTO VELOCIDADE ':'VENTO VELOCIDADE .0',
                                    'VENTO, DIRECAO (graus)': 'VENTO, DIRECAO (graus).0',
                                    'VENTO, RAJADA MAXIMA (m/s)':'VENTO, RAJADA MAXIMA (m/s).0',
                                    'RADIACAO GLOBAL (KJ/M2)':'RADIACAO GLOBAL (KJ/M2).0',
                                    'PRECIPITACAO (mm)':'PRECIPITACAO (mm).0'})
    return (table,table2)
                                
## Splitando data
def pivotandmerge(table,table2,station):
   
    df = pd.DataFrame(columns= ['Year','Month','Day','H(UTC)'])
    df['Year'] = pd.to_datetime(table['Unnamed: 0'][1:]).dt.year
    df['Month'] = pd.to_datetime(table['Unnamed: 0'][1:]).dt.month
    df['Day'] = pd.to_datetime(table['Unnamed: 0'][1:]).dt.day
    df['H(UTC)']=0
        
    df_horario = df
    for x in range(0,24):
        dftmp =df    
        dftmp['H(UTC)']=x
        df_horario = df_horario.append(dftmp)
    j=0
    
    for i in df_horario['H(UTC)'].unique():
        
        df_horario_tmp = df_horario.loc[df_horario['H(UTC)']==i]
      
        ## Tabela 1
        df_horario_tmp.loc[:,'TEMPERATURA DO AR (C)']                      = table.loc['1':,str('TEMPERATURA DO AR (C).'+str(i))]
        df_horario_tmp.loc[:,'TEMPERATURA MAXIMA (C)']                     = table.loc['1':,str('TEMPERATURA MAXIMA (C).'+str(i))]
        df_horario_tmp.loc[:,'TEMPERATURA MINIMA (C)']                     = table.loc['1':,str('TEMPERATURA MINIMA (C).'+str(i))]
        
        df_horario_tmp.loc[:,'UMIDADE RELATIVA DO AR (%)']                  = table.loc['1':,str('UMIDADE RELATIVA DO AR (%).'+str(i))]       
        df_horario_tmp.loc[:,'UMIDADE RELATIVA DO MAXIMA AR (%)']           = table.loc['1':,str('UMIDADE RELATIVA MAXIMA DO AR (%).'+str(i))]
        df_horario_tmp.loc[:,'UMIDADE RELATIVA DO MINIMA AR (%)']           = table.loc['1':,str('UMIDADE RELATIVA MINIMA DO AR (%).'+str(i))]
        
        df_horario_tmp.loc[:,'TEMPERATURA DO PONTO DE ORVALHO (C)']        = table.loc['1':,str('TEMPERATURA DO PONTO DE ORVALHO (C).'+str(i))]    
        df_horario_tmp.loc[:,'TEMPERATURA MÍNIMA DO PONTO DE ORVALHO (C)'] = table.loc['1':,str('TEMPERATURA MINIMA DO PONTO DE ORVALHO (C).'+str(i))]    
        df_horario_tmp.loc[:,'TEMPERATURA MÁXIMA DO PONTO DE ORVALHO (C)'] = table.loc['1':,str('TEMPERATURA MAXIMA DO PONTO DE ORVALHO (C).'+str(i))]
        
        ## Tabela 2
        df_horario_tmp.loc[:,'PRESSAO ATMOSFERICA (hPa)']                   = table2.loc['1':,str('PRESSAO ATMOSFERICA (hPa).'+str(i))]
        df_horario_tmp.loc[:,'PRESSAO ATMOSFÉRICA MAXIMA (hPa)']            = table2.loc['1':,str('PRESSAO ATMOSFERICA MAXIMA (hPa).'+str(i))]
        df_horario_tmp.loc[:,'PRESSAO ATMOSFÉRICA MINIMA (hPa)']            = table2.loc['1':,str('PRESSAO ATMOSFERICA MINIMA (hPa).'+str(i))]
        
        df_horario_tmp.loc[:,'VENTO VELOCIDADE ']                           = table2.loc['1':,str('VENTO VELOCIDADE .'+str(i))]
        df_horario_tmp.loc[:,'VENTO, DIRECAO (graus)']                      = table2.loc['1':,str('VENTO, DIRECAO (graus).'+str(i))]
        df_horario_tmp.loc[:,'VENTO, RAJADA MAXIMA (m/s)']                  = table2.loc['1':,str('VENTO, RAJADA MAXIMA (m/s).'+str(i))]
        
        df_horario_tmp.loc[:,'PRECIPITACAO (mm)']                           = table2.loc['1':,str('PRECIPITACAO (mm).'+str(i))]
        
        if i>=9 and i<=22:
                
            df_horario_tmp.loc[:,'RADIACAO GLOBAL (KJ/M2)']                    = table2.loc['1':,str('RADIACAO GLOBAL (KJ/M2).'+str(j))]
            j+=1
        
        if i==0:
            df_tmp = df_horario_tmp
        else:
            df_tmp = df_tmp.append(df_horario_tmp)
        #del df_horario_tmp
    
    df_tmp.loc [:,'Latitude']             = station['Latitude']            [station.index[0]]
    df_tmp.loc [:,'Longitude']            = station['Longitude']           [station.index[0]]
    df_tmp.loc [:,'Altitude(metros)']     = station['Altitude(metros)']    [station.index[0]]
    df_tmp.loc [:,'Nome']                 = station['Nome']                [station.index[0]]
    df_tmp.loc [:,'Codigo OMM']           = station['Codigo OMM']          [station.index[0]]
   
   ## Ordenando pela data e hora
    df_tmp                          = df_tmp.sort_values(by=['Year','Month','Day','H(UTC)'])
    df_tmp                          = df_tmp.set_index(['Year','Month','Day','H(UTC)'])
    
    #df_tmp.to_csv('/home/leonoro/Documents/Leandro/_AM_A134_S._G._DA_CACHOEIRA.csv')
    return (df_tmp)

if "__init__":
## Criando os dataframes 
    path = '/media/leandro/BKP/Documentos/IC/Tempo-Clima/Dados/EMA/PR/'
    stations = pd.read_csv('./dadosestações_f2.csv')
    errors = open('./nao-encontrado.txt','a')

    for (dirpath, dirnames, filenames) in walk('./TESTE'):
        #print(dirpath)        
        #print(dirnames)
        if filenames !=[] and dirpath.find('join')==-1:
            filenames.sort()
            i=0
            while(i<len(filenames)):
                station_data = stations[stations['Nome'].str.contains(filenames[i].split('_')[2])]
                if(station_data.empty):
                    errors.write(filenames[i] + " não encontrado\n")
                else:
                    table_16,table2_16 = change_name_columns(str(dirpath+'/'+filenames[i])  , str(dirpath+'/'+filenames[i+1]) )
                    table,table2       = change_name_columns(str(dirpath+'/'+filenames[i+2]), str(dirpath+'/'+filenames[i+3]) )
                    df_old = pivotandmerge(table,table2,station_data)
                    df_16  = pivotandmerge(table_16,table2_16,station_data)
                    df_old = df_old.append(df_16)
                    df_old.to_csv(str(dirpath+'/join/'+filenames[i]+'_join.csv'))
                    #df_16.to_csv(str(dirpath+'/join/'+filenames[i]+'_join.csv'))
                    print(filenames[i])                
                i+=4              
            print(dirpath)
    errors.close()     