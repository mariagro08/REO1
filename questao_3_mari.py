##### Questão 3.a #####

import numpy as np

##### Questão 3.a #####

def media (vetor):
    somador = 0
    dados = 0
    it = 0
    for el in vetor:
        somador = somador + el
        it = it + 1
        dados = dados + 1
        mean = somador/dados
    return mean

def var_amostral (vetor):
    somador = 0
    it = 0
    sdq = 0
    for el in vetor:
        somador = somador + el
        it = it + 1
        sdq = sdq + el**2
    var = (sdq - ((somador**2/it)))/(it-1)
    return var
print(' ')