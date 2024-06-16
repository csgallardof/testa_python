import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página web de IMDb con las 250 mejores películas
url = "https://www.imdb.com/chart/top"

# Hacer la solicitud GET a la página web
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Analizar el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar el contenedor principal con la lista de películas
    movie_table = soup.find('tbody', class_='lister-list')
    movies = movie_table.find_all('tr')
    
    # Listas para almacenar los datos
    titles = []
    years = []
    ratings = []
    
    # Extraer información de cada película
    for movie in movies:
        title_column = movie.find('td', class_='titleColumn')
        title = title_column.a.text
        year = title_column.span.text.strip('()')
        rating = movie.find('td', class_='ratingColumn imdbRating').strong.text
        
        titles.append(title)
        years.append(year)
        ratings.append(rating)
    
    # Crear un DataFrame con los datos
    df = pd.DataFrame({
        'Title': titles,
        'Year': years,
        'Rating': ratings
    })
    
    # Mostrar las primeras filas del DataFrame
    print(df.head())

    # Guardar los datos en un archivo CSV
    df.to_csv('imdb_top_250.csv', index=False)
else:
    print(f"Error al acceder a la página: {response.status_code}")
