# Importar librerias
import pandas as pd

# Cargar datos
df = pd.read_excel("C:/Users/uriel/OneDrive/Escritorio/Semestres/9nosemestre/Clasificacion de datos/datos2.xlsx")
df.head(2)

# Seleccionar variables
variable_x = "Advertising"
variable_y = "Sales"
n = "n"
Ex = "Ex"
Ey = "Ey"
Ex2 = "Ex2"
Exy = "Exy"
Excubo = "Ex-cubo"
nEx2 = "nEx2"
nExy = "nExy"

# a
modeloa = (((df[Ey] * df[Ex2]) - (df[Ex] * (df[Exy]))) / ((df[nEx2]) - (df[Excubo])))
print('\n''a: ', modeloa[0])
a = modeloa

# b
modelob = (((df[nExy]) - (df[Ex] * df[Ey])) / (df[nEx2] - df[Excubo]))
print('b: ', modelob[0])
b = modelob

# Y= a + bX
print('Y= ', round(modeloa[0], 2), '+', round(modelob[0], 2), 'X', )

# predicciones

dato_predictor = 20

print('\n', 'Valor X= ', dato_predictor)

# print('Prediction= ', (round(a[0], 2) + (round(b[0], 2) * dato_predictor)))
print('Prediction= ', round(a[0] + (b[0] * dato_predictor), 4))
# print('Prediction= ', (a[0] + (b[0] * dato_predictor)))
