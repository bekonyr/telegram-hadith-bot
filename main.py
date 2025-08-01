import logging
import os
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Хадистерди окуу функциясы
def load_hadiths(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

# Хадисттер жүктөлөт
HADITHS = load_hadiths('hadiths.txt')

# Тест үчүн 10 секунд интервал менен жиберүү
INTERVAL = 10  # секунд (реал иштөөдө 86400 кылса болот)

# Логгер
logging.basicConfig(level=logging.INFO)

# Колдонуучулар тизмеси
user_ids = set()

# /start буйругу
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    user_ids.add(user_id)
    await context.bot.send_message(chat_id=user_id, text="Ассаламу алейкум! Хадистерди жөнөтүүгө даярмын.")

# Хадист жөнөтүү цикл
async def send_hadiths_daily(application):
    while True:
        for user_id in user_ids:
            for hadith in HADITHS:
                try:
                    await application.bot.send_message(chat_id=user_id, text=hadith)
                    time.sleep(INTERVAL)
                except Exception as e:
                    logging.error(f"Хаталык: {e}")
        await asyncio.sleep(INTERVAL)

# Башкы функция
async def main():
    application = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    application.add_handler(CommandHandler("start", start))
    import asyncio
    asyncio.create_task(send_hadiths_daily(application))
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
