import requests
from bs4 import BeautifulSoup
from telegram import Bot
import asyncio

# URL de la página de Mercado Libre
url = 'https://www.mercadolibre.com.ec/samsung-galaxy-s20-ultra-5g-5g-128-gb-cosmic-black-12-gb-ram/p/MEC15482213?pdp_filters=item_id:MEC549016794#is_advertising=true&searchVariation=MEC15482213&position=1&search_layout=stack&type=pad&tracking_id=93980c60-e1fe-4e6b-a25b-830890555499&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=1&ad_click_id=MWFmYWY2YWYtZDdhZS00ZjJkLThhYjUtYTM5OGY3M2M1NTUy'

# Hacemos una solicitud HTTP a la página web
response = requests.get(url)

# Verificamos que la solicitud fue exitosa
if response.status_code == 200:
    # Obtenemos el contenido de la página
    page_content = response.content
    
    # Analizamos el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Buscamos el elemento que contiene el precio
    precio_elemento = soup.find('span', class_='price-tag-fraction')
    precio = precio_elemento.get_text() if precio_elemento else 'No se pudo obtener el precio'
else:
    precio = 'Error al acceder a la página: ' + str(response.status_code)

# Token del bot de Telegram (reemplázalo con tu propio token)
TOKEN = '7011037427:AAGQJ1mPdR8pxEoMv0aYE2_gu1BxiOLU0CM'
# ID del chat (reemplázalo con tu propio chat ID)
CHAT_ID = '596584999'

# Función asincrónica para enviar el mensaje de Telegram
async def enviar_mensaje():
    bot = Bot(token=TOKEN)
    mensaje = f'El precio del Samsung Galaxy S20 Ultra en Mercado Libre es: {precio}'
    await bot.send_message(chat_id=CHAT_ID, text=mensaje)

# Ejecutamos la función asincrónica
asyncio.run(enviar_mensaje())
