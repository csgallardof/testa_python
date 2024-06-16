import pandas as pd
import requests
import matplotlib.pyplot as plt

# URL de la API de COVID-19
url = "https://api.covid19api.com/dayone/country/ecuador/status/confirmed/live"

# Hacer la solicitud GET a la API
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Convertir los datos a formato JSON
    data = response.json()

    # Convertir los datos JSON a un DataFrame de pandas
    df = pd.DataFrame(data)

    # Convertir la columna 'Date' a un tipo de datos datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Seleccionar solo las columnas importantes
    df = df[['Date', 'Cases']]

    # Describir el DataFrame
    print(df.describe())

    # Configurar el tamaño de la figura
    plt.figure(figsize=(10, 5))

    # Plot de los casos confirmados a lo largo del tiempo
    plt.plot(df['Date'], df['Cases'], marker='o', linestyle='-')

    # Título y etiquetas del gráfico
    plt.title('Casos confirmados de COVID-19 en Ecuador')
    plt.xlabel('Fecha')
    plt.ylabel('Número de casos confirmados')
    plt.grid(True)
    plt.xticks(rotation=45)

    # Mostrar el gráfico
    plt.show()
else:
    print('Error al acceder a la API:', response.status_code)
