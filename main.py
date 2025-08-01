import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

# Хадистерди жүктөө
def load_hadiths():
    with open("hadiths.txt", "r", encoding="utf-8") as f:
        return f.read().split("\n\n")

hadiths = load_hadiths()

# /start буйругу
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ассаламу алейкум! Хадис алуу үчүн /hadis деп жазыңыз.")

# /hadis буйругу
async def hadis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hadith = random.choice(hadiths)
    await update.message.reply_text(hadith)

def main():
    application = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("hadis", hadis))
    application.run_polling()

if __name__ == "__main__":
    main()
