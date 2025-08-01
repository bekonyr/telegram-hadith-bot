import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Салам! Хадис бот иштеп жатат.")

def main():
    application = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
