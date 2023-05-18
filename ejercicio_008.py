import pandas as pd

notas = {'Juan':9, 'Maria':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis':5}

def aprobados(notas):
    df = pd.Series(notas)
    aprobados = df[df>= 6].sort_values(ascending = False)

print(aprobados(notas))






