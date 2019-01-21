#!/usr/bin/python

import numpy as np
import pandas as pd
from scipy.io import loadmat

'''Constructing a pandas dataframe from a matlab .mat file'''
data_set = loadmat("data_set.mat")

print data_set.keys()

rows = data_set['rows']
dataVal = data_set['data']
data_dict = {}

for i,v in enumerate(rows):
    data_dict[v[0][0]] = dataVal[i]

df = pd.DataFrame(data=data_dict)
