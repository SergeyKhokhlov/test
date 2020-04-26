from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

TOKEN = "1213926896:AAGeW9NZeh6AJebSQCyudrMcy10hQdfuH0E"


def start(update, context):
    reply_keyboard = [["Написать отзыв", "Написать в техническую поддержку"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text("Этому боту вы можете написать нам свой отзыв о нашем сайте"
                              " или обратиться в техническую поддержку", reply_markup=markup)


def write_feedback(update, context):
    reply_keyboard = [["Написать отзыв", "Написать в техническую поддержку"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text("Вы можете написать любой отзыв о нас!", reply_markup=markup)


def write_about_error(update, context):
    reply_keyboard = [["Написать отзыв", "Написать в техническую поддержку"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text("Мы обязательно поможем вам! Напишите подробно о вашей ошибки!",
                              reply_markup=markup)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.regex("Написать отзыв"),
                                  write_feedback))
    dp.add_handler(MessageHandler(Filters.regex("Написать в техническую поддержку"),
                                  write_about_error))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
