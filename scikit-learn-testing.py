# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 16:33:57 2022

@author: bernardogoltz
@title: testing sci-kit learn

""" 
import pandas as pd

# importando datasets pelo link
uri_diabetes = "https://gist.githubusercontent.com/davidneves11/944edb5ecb7bf6d1770eae91cb20d049/raw/50d3d054185815b0c49561f94badedc06ef3c313/diabetes.csv"

uri_colesterol = "https://gist.githubusercontent.com/davidneves11/01b2963f7a8dfd87d79010fbf847b221/raw/685870f4365bcda4e5bb9e342285e0aac37dd556/colesterol.csv"

uri_batimentos = "https://gist.githubusercontent.com/davidneves11/d72e7f49ab01c856acc5d07be4b1a9dd/raw/37631e3a40da92e6261c00fffdf0fb9b869b35dd/batimentos%2520cardiacos.csv"

# lendo os datasets --- pandas
diabetes = pd.read_csv(uri_diabetes)
colesterol = pd.read_csv(uri_colesterol)
batimentos = pd.read_csv(uri_batimentos)

descr = diabetes.describe() # cria variavel que da caracteristicas (abordagem estatistica) do dataset
tamanho = diabetes.shape # dupla observações x características
 


#⁕⁕⁕treinando os dados:⁕⁕⁕

from sklearn.model_selection import train_test_split # importando

x = diabetes['idade']
y = diabetes['resultado']

x_treino , x_teste , y_treino , y_teste = train_test_split(x,y)

# gera 4 valores ordenados
#[75%] X_TREINO , X_TESTE , 
#[25%] Y_TREINO , Y_TESTE


# classificação: y = 0 ou 1. 
 

