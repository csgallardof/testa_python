import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página a hacer scraping
url = "https://listado.mercadolibre.com.ec/celulares#D[A:celulares]"

# Realizar la solicitud HTTP a la URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Listas para almacenar los datos
titles = []
prices = []

# Extraer la información de los productos
for product in soup.find_all('li', class_='ui-search-layout__item'):
    try:
        title = product.find('h2', class_='ui-search-item__title').text.strip()
        price = product.find('span', class_='price-tag-fraction').text.strip()
        titles.append(title)
        prices.append(price)
    except AttributeError:
        continue

# Crear un DataFrame con los datos obtenidos
df = pd.DataFrame({'Title': titles, 'Price': prices})

# Guardar el DataFrame en un archivo CSV
df.to_csv('mercadolibre_celulares.csv', index=False)

print("Datos extraídos y guardados en mercadolibre_celulares.csv")
