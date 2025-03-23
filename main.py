
from telegram_bot import send_message
from trading_logic import run_trading_bot

if __name__ == "__main__":
    send_message("🤖 Bot de trading iniciado.")
    run_trading_bot()
