# -*- coding: utf-8 -*-

"""
    1 - eh gordinho?
    2 - perna curta?
    3 - faz auau?
"""

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()

porco1 = [1,1,0]
porco2 = [1,1,0]
porco3 = [1,0,0]

cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]

dados =  [porco1 , porco2 , porco3,
          cachorro1, cachorro2, cachorro3]

marcacoes = [1,1,1,-1,-1,-1]

misterioso = [1,1,1]

modelo.fit(dados , marcacoes)
# tentarr se encaixar as informacoes dadas 
# (x,y)
