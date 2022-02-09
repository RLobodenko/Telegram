
import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

MESSAGE,  MESSAGE1, MESSAGE_2, MESSAGE_3 = range(4)


def start(update: Update, context: CallbackContext) -> int:

    reply_keyboard = [['Столы', 'Этажерки', 'Стойки']]

    update.message.reply_text(


        'Выберите мебель',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True,
        ),
    )

    return MESSAGE







def message(update: Update, context: CallbackContext) -> int:

    user = update.message.from_user
    logger.info("Message of %s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        'Какой номер позиции? ',
        reply_markup=ReplyKeyboardRemove(),
    )


    return MESSAGE_2



def message_3(update: Update, context: CallbackContext) -> int:

    user = update.message.from_user
    logger.info("Message_3 of %s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        'Какое количество и куда доставить? ',
        reply_markup=ReplyKeyboardRemove(),
    )


    return MESSAGE_3

def start1(update: Update, context: CallbackContext) -> int:

    reply_keyboard = [['Новогодние украшения 🎄', 'Каталог мебели 🪑', 'Бесплатная доставка 📦']]

    update.message.reply_text(


        'Выберите подарок 🎁',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True,
        ),
    )



    return MESSAGE1


def message_2(update: Update, context: CallbackContext) -> int:

    user = update.message.from_user
    logger.info("Message_2 of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Спасибо! Ваш заказ принят')

    return ConversationHandler.END




def main() -> None:


    updater = Updater("2029998715:AAFEGCFt1Xmr0edpjT_vI0WwzXPkqgDmFBU")


    dispatcher = updater.dispatcher


    assert isinstance(MESSAGE, object)

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            MESSAGE: [MessageHandler(Filters.regex('^(Столы|Этажерки|Стойки)$'), message)],


            MESSAGE_2: [MessageHandler(Filters.text & ~Filters.command, message_3)],

            MESSAGE_3: [MessageHandler(Filters.text & ~Filters.command, start1)],

            MESSAGE1: [MessageHandler(Filters.regex('^(Новогодние украшения 🎄|Каталог мебели 🪑|Бесплатная доставка 📦)$'), message_2)],
        },
        fallbacks=[CommandHandler('message_2', message_2)],
    )

    dispatcher.add_handler(conv_handler)


    updater.start_polling()


    updater.idle()


if __name__ == '__main__':
    main()