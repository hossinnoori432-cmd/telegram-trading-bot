import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# ======================
# CONFIG
# ======================

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

SCAN_INTERVAL = 300  # 5 minutes

# ======================
# LOGGING
# ======================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ======================
# COMMAND HANDLERS
# ======================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Trading Bot is LIVE!\n\n"
        "📊 Markets: Crypto & Forex\n"
        "⏱ Timeframes: 15m / 30m / 1h\n"
        "🔔 Signals are sent automatically\n\n"
        "⚠️ Not financial advice"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Commands:\n"
        "/start - Start the bot\n"
        "/help - Show help\n\n"
        "Signals are sent automatically when conditions are met."
    )

# ======================
# MARKET SCANNER (TEST)
# ======================

async def scan_market(context: ContextTypes.DEFAULT_TYPE):
    message = (
        "📊 BTCUSDT (30m)\n\n"
        "Signal: 🟡 HOLD\n"
        "Price: 89500.00\n"
        "RSI: 9.97\n"
        "MA20: 90247.36\n"
        "MA50: 91281.46\n\n"
        "⚠️ Not financial advice"
    )

    await context.bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )

# ======================
# MAIN
# ======================

def main():
    print("✅ Trading bot running...")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.job_queue.run_repeating(
        scan_market,
        interval=SCAN_INTERVAL,
        first=10
    )

    app.run_polling()

# ======================
# ENTRY POINT
# ======================

if __name__ == "__main__":
    main()
