# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 18:59:52 2022

@author: angel
"""
import pandas as pd 

uri_colesterol = "https://gist.githubusercontent.com/davidneves11/01b2963f7a8dfd87d79010fbf847b221/raw/685870f4365bcda4e5bb9e342285e0aac37dd556/colesterol.csv"

colesterol = pd.read_csv(uri_colesterol)