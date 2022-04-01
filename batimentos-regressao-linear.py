# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 18:18:25 2022

@ title : batimentos cardiacos

"""

# importando a biblioteca: 
    
import pandas as pd 

uri_batimentos = "https://gist.githubusercontent.com/davidneves11/d72e7f49ab01c856acc5d07be4b1a9dd/raw/37631e3a40da92e6261c00fffdf0fb9b869b35dd/batimentos%2520cardiacos.csv"

batimentos = pd.read_csv(uri_batimentos)


# separando os registros de varíaveis dependentes (conclusão.)
x = batimentos[['Idade' , 'Peso']]
y = batimentos['Batimentos cardiacos']

import seaborn as sns

sns.lmplot(x = 'Peso', y = 'Batimentos cardiacos',  data = batimentos , line_kws = {'color':'red'})

sns.lmplot(x = 'Idade', y = 'Batimentos cardiacos',  data = batimentos , line_kws = {'color':'red'})

# criando o modelo de regressão linear: 
    
from sklearn.model_selection import train_test_split

x_treino , x_teste , y_treino , y_teste = train_test_split(x , y)

from sklearn import linear_model

rgs = linear_model.LinearRegression(fit_intercept = False , normalize = True)

modelo_linear = rgs.fit(x_treino , y_treino)
acuracia_modelo = rgs.score(x_teste , y_teste)





