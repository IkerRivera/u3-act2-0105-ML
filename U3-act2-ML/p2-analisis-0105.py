
import pandas as pd
import numpy as np
print("analisis de datos alumno Iker Montoya 0105 ")

transacciones = {
    "Id_Transaccion": ["T001", "T002", "T003", "T004", "T005", "T006"],
    "Monto": [15.50, 2500.00, 45.00, 890.00, 45.00, 3400.00],
    "Ubicacion_Inusual": [False, True, False, True, False, True],
    "Es_Fraude": [False, True, False, False, False, True]
}
df = pd.DataFrame(transacciones)
print(df)
print("-+-+-+-+-+--+agrupar por una sola columna Es_Fraude -+--+-+-+-+--+-+-")
agrupados = df.groupby('Es_Fraude')
print(agrupados)
print("-+-+-+-+-+--+agrupar por agregacion Es_Fraude -+--+-+-+-+--+-+-")
# Average monto by fraude
print(agrupados['Monto'].mean())

# Maximum monto in each fraude
print(agrupados['Monto'].max())
