import pandas as pd
from telegram import Bot
from telegram.error import TelegramError
import asyncio

# Token del bot (obténlo de BotFather)
TOKEN = '7011037427:AAGQJ1mPdR8pxEoMv0aYE2_gu1BxiOLU0CM'
CHAT_ID = '596584999'

async def send_message(token, chat_id, message):
    bot = Bot(token=token)
    try:
        await bot.send_message(chat_id=chat_id, text=message)
        print("Mensaje enviado a Telegram")
    except TelegramError as e:
        print(f"Error al enviar mensaje: {e}")

async def main():
    # Leer el archivo CSV
    try:
        df = pd.read_csv('mercadolibre_celulares.csv')
    except FileNotFoundError:
        print("El archivo 'mercadolibre_celulares.csv' no se encuentra.")
        return

    # Crear el mensaje a enviar
    message = "Lista de celulares en Mercado Libre:\n\n"
    for index, row in df.iterrows():
        message += f"Producto: {row['Title']}\nPrecio: {row['Price']}\n\n"
    
    # Enviar el mensaje usando el bot
    await send_message(TOKEN, CHAT_ID, message)

if __name__ == "__main__":
    asyncio.run(main())
