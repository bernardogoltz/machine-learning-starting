# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 17:24:14 2022

@bernardogoltz
@title: classificação diabetes. 

"""

import pandas as pd 

uri_diabetes = "https://gist.githubusercontent.com/davidneves11/944edb5ecb7bf6d1770eae91cb20d049/raw/50d3d054185815b0c49561f94badedc06ef3c313/diabetes.csv"

diabetes = pd.read_csv(uri_diabetes)

# criar dataset com os registros, mas sem a conclusão de classificação. método drop. 

x = diabetes.drop('resultado' , axis = 1) 

y = diabetes.resultado


from sklearn.model_selection import train_test_split

SEED = 4121988 # seed aleatória usada pelos instrutores do treinamento. 

x_treino , x_teste , y_treino , y_teste = train_test_split(x , y) 

from sklearn.tree import DecisionTreeClassifier
from sklearn.dummy import DummyClassifier

clf_arvore = DecisionTreeClassifier(random_state = SEED , max_depth = 3)

modelo = clf_arvore.fit(x_treino , y_treino) # aprende com x treino e y treino 

modelo_acuracia = modelo.score(x_teste , y_teste)
print(round(modelo_acuracia,4)*100)

modelo_dummy = DummyClassifier(strategy = 'most_frequent')
modelo_dummy.fit(x_treino , y_treino)
modelo_dummy_acuracia = modelo_dummy.score(x_teste , y_teste)
print(round(modelo_dummy_acuracia,4)*100)


