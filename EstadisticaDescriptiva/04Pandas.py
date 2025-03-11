import pandas as pd

df=pd.read_csv('./EstadisticaDescriptiva/housing.csv')


#mostrar las primeras 5 filas
print(df.head())

#las ultimas 5 filas
print(df.tail())

#Quiero una fila en especifico
print(df.iloc[7])

#Mostrar una columna por su nombre

print(df["ocean_proximity"])

#obtener la media de la columna del total de cuartos

mediacuartos =df["total_rooms"].mean()

#Quiero obtener la mediana de la columna population

medianapopularidad=df["population"].median()

print('mediana de popularidad: ', medianapopularidad)

std_age=df["housing_median_age"].std()
print('Desviacion Estandar de años: ', std_age)


#Para poder filtrar

filtrodeloceano=df[df["ocean_proximity"]=="ISLAND"]
print('Filtro de proximidad del oceano: ', filtrodeloceano)




