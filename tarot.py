from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import datetime


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Пожалуйста, введите свою дату рождения в формате DD.MM.YYYY")


# Функция для обработки введенной даты рождения
def calculate_card(update: Update, context: CallbackContext):
    birth_date = update.message.text

    try:
        day, month, year = map(int, birth_date.split('.'))
        total_sum = day // 10 + day % 10 + month // 10 + month % 10 + year // 1000 + (year // 100) % 10 + (
                    year // 10) % 10 + year % 10
        if total_sum > 22:
            total_sum = total_sum - 22

        # Определение карты старших аркан
        major_arcana = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
                        "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune",
                        "Justice", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star",
                        "The Moon", "The Sun", "Judgement", "The World"]

        card_name = major_arcana[total_sum - 1]

        update.message.reply_text(f"Ваша карта старших аркан: {card_name}")

        # Можете добавить небольшое описание карты

    except ValueError:
        update.message.reply_text("Похоже, вы ввели неверный формат даты. Пожалуйста, попробуйте снова.")


# Основная функция
def main():
    updater = Updater("YOUR_API_TOKEN", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, calculate_card))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()