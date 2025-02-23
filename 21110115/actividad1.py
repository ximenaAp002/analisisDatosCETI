import pandas as pd

s = pd.Series([1, 3, 5, 7, 9])
print(s)

data = {'Nombre': ['Ana', 'Luis', 'Carlos'],
        'Edad': [23, 30, 25],
        'Ciudad': ['CDMX', 'Monterrey', 'Guadalajara']}
df = pd.DataFrame(data)
df

print("--------------------------Data set-------------------------")
print(df)

df.to_csv("nombre-edad-ciudad.csv", index=False)
print("---------------------------dataset de videojuegos-----------------")

df = pd.read_csv("vgchartz-2024.csv")  # Leer un CSV
print(df)

#df.to_excel("archivo_nuevo.xlsx", index=False)

print("----------------------inspeccionar dataframe--------------------------")

df.head()  # Muestra las primeras 5 filas
df.tail()  # Muestra las últimas 5 filas
df.info()  # Información general del DataFrame
df.describe()  # Estadísticas descriptivas
df.shape  # Tamaño del DataFrame (filas, columnas)

print("----------------------seleccion de datos------------------")

print(df["title"])

print(df[["title","console","total_sales"]])
print("------------------------------filtrado de datos----------------------")

print(df.iloc[1000],"\n-----------------\n",df.loc[1000]   )  # Primera fila (index basado en posición)
        # Primera fila (index basado en etiquetas

print("modificar datos: \nañadir una columna")

df["nueva_columna"]=[123,435435,345435]

print("----------------Eliminar columnas o filas---------------")

df.drop(columns=["nueva_columna"], inplace=True)  # Eliminar columna
df.drop(index=0, inplace=True)  # Eliminar primera fila
print("----------------renombrar columnas----------------")
df.rename(columns={"title": "titulo"}, inplace=True)

print("-----------------manejo de valores nulos-----------------------------")

df.isnull().sum()  # Contar valores nulos por columna
df.dropna(inplace=True)  # Eliminar filas con valores nulos
df.fillna("Desconocido", inplace=True)  # Rellenar valores nulos


print("------------------operaciones estadisticas-----------------")

df["total_sales"].mean()  # Promedio
df["total_sales"].sum()   # Suma total
df["total_sales"].min()   # Mínimo
df["total_sales"].max()   # Máximo
df["total_sales"].std()   # Desviación estándar}}



print("------------------agrupacion de datos-----------------")

df.groupby("console")["total_sales"].mean()  # Promedio de edad por ciudad


print("------------------ordenar valores-----------------")
df.sort_values(by="na_sales", ascending=False, inplace=True)  # Ordenar por edad descendente