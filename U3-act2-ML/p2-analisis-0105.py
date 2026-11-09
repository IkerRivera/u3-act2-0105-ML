# importar librerias
import pandas as pd
import numpy as np

print("Analisis de datos transacciones Iker Montoya NC=0105")

transacciones = {
    "Id_Transaccion": ["T001", "T002", "T003", "T004", "T005", "T006"],
    "Monto": [15.50, 2500.00, 45.00, 890.00, 12.00, 3400.00],
    "Ubicacion_Inusual": [False, True, False, True, False, True],
    "Es_Fraude": [False, True, False, False, False, True]
}

df = pd.DataFrame(transacciones)
print(df)

print("-+--++--+-+ AGRUPAR COLUMNAS -+-+-+-+-+-+-+-+")
agrupado = df.groupby('Ubicacion_Inusual')
print(agrupado)

print("-+--++--+-+ POR AGREGACION -+-+-+-+-+-+-+-+")

# Es_Fraude
print(agrupado['Es_Fraude'].mean())

print("-+-+-+-+--+ Monto maximo -++-+--++-+-+--++")

# Monto
print(agrupado['Monto'].max())

print("Iker-+-+-+-++-+ segunda parte -+-+-+-+-+-+0105")
print("Agregaciones multiples ")
print("mean --> promedio, sum --> suma")
print("max --> maximo, min --> minimo")

resultado_agregado = agrupado['Monto'].agg(['mean', 'sum', 'max', 'min'])
print(resultado_agregado)

print("Agrupacion por varias columnas")
print("Agrega columna al dataframe")
print("columna tipo --> fraude")

df['tipo'] = ['Normal', 'Fraude', 'Normal', 'Normal', 'Normal', 'Fraude']

agrupado_multiple = df.groupby(['Ubicacion_Inusual', 'tipo'])['Monto'].mean()
print(agrupado_multiple)