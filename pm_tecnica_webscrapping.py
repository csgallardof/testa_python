import requests
from bs4 import BeautifulSoup

# URL de la página web a la que queremos hacer scraping
url = 'https://www.computron.com.ec/'

# Hacemos una solicitud HTTP a la página web
response = requests.get(url)

# Verificamos que la solicitud fue exitosa
if response.status_code == 200:
    # Obtenemos el contenido de la página
    page_content = response.content
    
    # Analizamos el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Buscamos todos los elementos que contienen precios
    precios = soup.find_all('span', class_='price')
    
    # Recolectamos y mostramos los precios
    for precio in precios:
        print(precio.get_text())
else:
    print('Error al acceder a la página:', response.status_code)
