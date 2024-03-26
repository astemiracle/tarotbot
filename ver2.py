from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Функция обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Пожалуйста, введите вашу дату рождения в формате DD.MM.YYYY.')

# Функция обработки текстовых сообщений
def handle_message(update: Update, context: CallbackContext) -> None:
    birth_date = update.message.text
    card_number = calculate_tarot_card(birth_date)
    description = get_tarot_card_description(card_number)
    update.message.reply_text(f"Ваша карта Таро: {card_number}\nОписание карты: {description}")

# Функция вычисления карты Таро
def calculate_tarot_card(birth_date):
    day, month, year = map(int, birth_date.split('.'))

    total = day + day + month + month + year + year + year + year

    if total > 22:
        total -= 22

    return total

# Функция получения описания карты Таро
def get_tarot_card_description(card_number):
    tarot_cards = {
        1: "Описание карты 1",
        2: "Описание карты 2",
        # Добавьте описания для остальных карт здесь
    }

    return tarot_cards.get(card_number, "Карта не найдена")

def main() -> None:
    updater = Updater("YOUR_TOKEN_HERE")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()