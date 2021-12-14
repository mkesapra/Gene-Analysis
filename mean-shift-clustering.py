#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 19:49:22 2020

@author: kesaprm
"""


import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
import pandas as pd 
from sklearn.datasets import make_blobs

centers = [[1, 1], [-1, -1], [1, -1]]
X, _ = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)

dfT1 = pd.read_excel("Mouse_Data1.xlsx", sheet_name='Tongue1')
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
dfT1.info()

from sklearn import svm
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)

clf.predict([[2., 2.]])