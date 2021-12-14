#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:57:08 2020

@author: kesaprm
"""

import numpy as np
import pandas as pd 
import tensorflow as tf
from mlxtend.frequent_patterns import apriori, association_rules

dfS1 = pd.read_excel("orthoMouseData1_MG.xlsx", sheet_name='Skin_Cleaned_AVG')

dfS1.info()

frq_items = apriori(dfS1, min_support = 0.05, use_colnames = True) 
