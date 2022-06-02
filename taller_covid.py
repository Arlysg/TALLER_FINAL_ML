# -*- coding: utf-8 -*-
"""
Created on Wed May 25 19:17:59 2022

@author: asanjuan14
"""

import pandas as pd
import matplotlib.pyplot as plt

url='Casos_positivos_de_COVID-19_en_Colombia_25052022.csv'

data= pd.read_csv(url)


#conocer direcciones del archivo
data.shape

#conocer las columnas del archivo

data.columns

#cantidad de elementos del archivo
data.size

#saber cuantos registros hay por columna
data.count()


#eliminar columnas

data['Código ISO del país']

data.drop('Código ISO del país', axis=1,inplace= True)
data.drop('Nombre del país', axis=1,inplace= True)
data.drop('Pertenencia étnica', axis=1,inplace=True)
data.drop('Nombre del grupo étnico', axis=1,inplace= True)
data.drop('Fecha de inicio de síntomas', axis=1,inplace= True)
data.drop('Unidad de medida de edad', axis=1,inplace= True)
data.drop('Código DIVIPOLA departamento', axis=1,inplace= True)
data.drop('Código DIVIPOLA municipio', axis=1,inplace= True)
data.drop('ID de caso', axis=1,inplace= True)


#Normalizar la columna de estado

data.loc[data['Estado']=='leve']='leve'
data.loc[data['Estado']=='LEVE']='leve'
data.loc[data['Sexo']=='m']='M'
data.loc[data['Sexo']=='f']='F'

#cuantas personas murieron por covid en colombia

cantidad_muertes=[(data['Estado']=='Fallecido')].shape[0]
print (cantidad_muertes)

#cantidad_muertes=data.loc[data['Estado']=='Fallecido']

#cuantas mujeres fallecieron en colombia

aux = data.loc[(data['Estado']=='Fallecido') & (data['Sexo']=='F')]
cantidad_mujeres_muertes = aux.shape[0]

#CUANTAS PERSONAS FALLECIERON EN BARRANQUILLA

aux = data.loc[(data['Estado']=='Fallecido') & (data['Nombre municipio']=='Barranquilla')]
cantidad_mujeres_muertes_mj_BQ = aux.shape[0]

#tasa de mortalidad del covid

cantidad_casos=data.shape[0]
tasa_mortalidad=cantidad_muertes/cantidad_casos*100

#agrupar por columnas
data.groupby('Sexo','Estado').size()



#listar por orden desecendete las ciudades con mas casos

data['Nombre municipio'].value_counts().head(10)


#curva de contagios en barranquilla 

data[data['Nombre municipio'] =='BARRANQUILLA'].groupby('Fecha de diagnóstico').size().plot()







