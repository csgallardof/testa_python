# Web Scraping y Envío de Datos a Telegram

Este proyecto realiza web scraping en Mercado Libre para obtener información sobre celulares, almacena los datos en un DataFrame y envía la información a un bot de Telegram.

## Instrucciones

1. Clona el repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`.
3. Ejecuta `scraping.py` para obtener los datos.
4. Configura tu bot de Telegram y añade tu token y chat_id en `send_telegram.py`.
5. Ejecuta `send_telegram.py` para enviar los datos a Telegram.

## Dependencias

- requests
- BeautifulSoup4
- pandas
- python-telegram-bot

## Ejecución

```bash
python pm_scraping.py
python pm_send_telegram.py

