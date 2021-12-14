#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 22:42:41 2020

@author: kesaprm
"""

import pandas as pd


df_skin_Up_1 = pd.read_csv('Gene_groups_skin/Upregulated_0-24-Table1.csv')

df_skin_Up_2 = pd.read_csv('Gene_groups_skin/Upregulated_24-120-Table1.csv')

df_skin_Up_3 = pd.read_csv('Gene_groups_skin/Upregulated_120-240-Table1.csv')


df_tongue_Up_1 = pd.read_csv('Gene_groups_tongue/Upregulated_0-24-Table1.csv')

df_tongue_Up_2 = pd.read_csv('Gene_groups_tongue/Upregulated_24-120-Table1.csv')

df_tongue_Up_3 = pd.read_csv('Gene_groups_tongue/Upregulated_120-240-Table1.csv')


df_skin_Up_1.fillna('0')
df_skin_Up_2.fillna('0')
df_skin_Up_3.fillna('0')


df_tongue_Up_1.fillna('0')
df_tongue_Up_2.fillna('0')
df_tongue_Up_3.fillna('0')

np_skin_Up_1 = df_skin_Up_1.to_numpy()
np_skin_Up_2 = df_skin_Up_2.to_numpy()

np_tongue_Up_1 = df_tongue_Up_1.to_numpy()


import numpy as np

out_arr = np.intersect1d(np_skin_Up_1, np_tongue_Up_1) 

print ("Output array: ", out_arr)  


