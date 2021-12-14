#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 04:25:50 2020

@author: kesaprm
"""

from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd 


dfT1 = pd.read_excel("Mouse_Data1.xlsx", sheet_name='Tongue1')

model = KMeans(n_clusters=3)

model.fit([dfT1['unwounded tongue'],dfT1['tongue, 6hrs post-wounding'],dfT1['tongue, 12hrs post-wounding']])


all_predictions = model.predict([dfT1['tongue, 24hrs post-wounding'],dfT1['tongue, 3days post-wounding']])

print(all_predictions)

##################hierarchial clustering####################
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

removedColumns = list(dfT1.pop('GB ACC'))
removedColumns2 = list(dfT1.pop('RefSeq Transcript ID'))
remCOl3 = list(dfT1.pop('Gene Symbol'))
remCOl4 = list(dfT1.pop('Gene Title'))



samples = dfT1.values

mergings = linkage(samples, method='complete')

dendrogram(mergings,
           labels=remCOl3,
           leaf_rotation=90,
           leaf_font_size=6,
           )

plt.show()