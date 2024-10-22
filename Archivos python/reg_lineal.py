import matplotlib.pyplot as plt # crear graficos
import seaborn as sns # crear graficos
import plotly.express as px # crear graficos interactivos
import numpy as np # manipulacion de vectores y matrices
import pandas as pd # manipulacion de los dataframes
import missingno as msno # visualizar los valores NAs
import pingouin as pg # paquete estadisico para test estadisticos: ANOVA, Chi, Square,...
import statsmodels.api as sm # paquete de modelos estadisticos potentes

# Cargar el dataset
data = pd.read_csv(r'Datasets\Parque Automotor\CRECIMIENTO_DEL_PARQUE_AUTOMOTOR_RUNT2.0_20241011.csv', header=0)

# Definir el umbral para considerar categorías "pequeñas"
umbral = 600

# Agrupar las categorías pequeñas bajo la etiqueta "otros"
frecuencias = data["NOMBRE_DE_LA_CLASE"].value_counts()
categorias_pequenas = frecuencias[frecuencias < umbral].index
data["NOMBRE_DE_LA_CLASE"] = data["NOMBRE_DE_LA_CLASE"].replace(categorias_pequenas, "OTROS")

print(data.head()) # Mostrar las primeras 5 filas
print(data.tail()) # Mostrar las ultimas 5 filas
data.info() # Mostrar los tipos de datos de las columnas
print(data.describe()) # De las variables cuantitativas me muestra valores estadisticos

# Numero de filas y observaciones
print('Numero de filas:')
print(len(data))

# Numero de columnas
print('Numero de columnas:')
print(len(data.columns))

# Columnas - nombres
print(pd.DataFrame(data.columns))

# seleccionando o filtrando datos a traves del metodo loc
print(data[["NOMBRE_DE_LA_CLASE","CANTIDAD"]][(data["NOMBRE_DE_LA_CLASE"]=="AUTOMOVIL")])
print(data[["NOMBRE_DE_LA_CLASE","CANTIDAD"]][(data["NOMBRE_DE_LA_CLASE"]=="CAMPERO")])
print(data[["NOMBRE_DE_LA_CLASE","CANTIDAD"]][(data["NOMBRE_DE_LA_CLASE"]=="CAMION")])
print(data[["NOMBRE_DE_LA_CLASE","CANTIDAD"]][(data["NOMBRE_DE_LA_CLASE"]=="MOTOCARRO")])
print(data[["NOMBRE_DE_LA_CLASE","CANTIDAD"]][(data["NOMBRE_DE_LA_CLASE"]=="MOTOCICLETA")])

# Visualización de la distribución de las clases de vehículos
plt.figure(figsize=(12,8))
sns.countplot(x="NOMBRE_DE_LA_CLASE", data=data, hue="NOMBRE_DE_LA_CLASE", palette="Set1", legend=False)
plt.title("Distribución de Clases de Vehículos")
plt.xticks(rotation=90)
plt.show()

# Visualización de las cantidades de vehículos por clase
plt.figure(figsize=(12,8))
sns.barplot(x="NOMBRE_DE_LA_CLASE", y="CANTIDAD", data=data, hue="NOMBRE_DE_LA_CLASE", palette="Set1", estimator=sum, legend=False)
plt.title("Cantidad de Vehículos por Clase")
plt.xticks(rotation=90)
plt.ylabel("Cantidad Total")
plt.show()
