# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:58:10 2020

@author: Andrej Košir
"""

import numpy as np
import pandas as pd

# Input data
A = [[0, 1, 1, 0, 0], 
     [0, 0, 1, 1, 0],
     [0, 0, 0, 1, 1],
     [0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]

BM = 100
C = [[0, 2, 4, BM, BM],
     [2, 0, 3, 1, BM],
     [4, 3, 0, 5, 3],
     [BM, 1, 5, 0, 2],
     [BM, BM, 3, 2, 0]]

s, t = 1, 5

# Shtani v datoteko
A_df = pd.DataFrame(A)
A_df.to_csv('matA.csv', index=False, header=False)
C_df = pd.DataFrame(C)
C_df.to_csv('matC.csv', index=False, header=False)
st_df = pd.DataFrame([s, t])
st_df.to_csv('st.csv', index=False, header=False)

A1 = pd.read_csv('matA.csv').to_numpy()


