#scipy.sparse.csgraph.maximum_flow
import numpy as np
import pandas
import funkcije as fn

matrika_sosednosti = pandas.read_csv('matA.csv',header=None).to_numpy()
matrika_kapacitet = pandas.read_csv('matC.csv', header=None).to_numpy()
izvor_ponor = pandas.read_csv('st.csv', header=None).to_numpy()
izvor = izvor_ponor[0][0]-1
ponor = izvor_ponor[1][0]-1
(matrika_prenosov, pot, maks) = fn.najvecji_pretok(matrika_sosednosti,matrika_kapacitet,izvor,ponor)
lab = {i:i+1 for i in range(len(matrika_prenosov))}
fn.narisi_grafa(matrika_prenosov,lab,pot)
print(maks)

