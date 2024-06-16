import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('ruta_al_archivo.csv')

# Exploración inicial de los datos
print(df.head())
print(df.info())
print(df.describe())

# Limpieza de datos
df.dropna(inplace=True)  # Eliminar filas con valores nulos
df.drop_duplicates(inplace=True)  # Eliminar filas duplicadas
df['columna'] = df['columna'].astype(int)  # Convertir una columna a entero
df.rename(columns={'columna_antigua': 'columna_nueva'}, inplace=True)  # Renombrar columna
df = df[df['columna'] > 10]  # Filtrar filas

# Guardar el DataFrame limpio en un nuevo archivo CSV
df.to_csv('ruta_al_archivo_limpio.csv', index=False)
