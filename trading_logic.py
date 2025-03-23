
import time
from telegram_bot import send_message

def run_trading_bot():
    while True:
        # Simulación de análisis y trade
        send_message("📈 Ejecutando análisis de mercado...")
        time.sleep(3600)  # Espera 1 hora (puedes cambiarlo por 60 seg o menos)
