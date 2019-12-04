from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import telegram
import logging
import os
from os.path import join, dirname
from controller import Controller

from player import Player
from predictor import Predictor
from converter import Converter
import time

TOKEN='971659272:AAF03CZJzlo0uLbuGJ6kprFW9dpTRttVFws'

logging.basicConfig(level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

env = os.environ.get('ENV', 'development')

controller = Controller()
player = Player()
predictor = Predictor()

try:
    def sayText(bot, update, texto):
        bot.send_message(chat_id=update.message.chat_id, text=texto, parse_mode=telegram.ParseMode.HTML)

    def echo(bot, update):
        goToNextStep = True

        answer = update.message.text
        print("Answer: " + answer)

        textos = controller.getText(answer)

        #when answer is None, means the answer was invalid
        if textos == None:
            textos = ["Cara, o que você escreveu não tem lógica, coesão, inteligência, digita de novo"]
            goToNextStep = False
        else: 
            player.fill(answer, controller.step)

        for texto in textos:
            bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
            time.sleep(2)
            bot.send_message(chat_id=update.message.chat_id, text=texto, parse_mode=telegram.ParseMode.HTML, action = telegram.ChatAction.TYPING)

        if goToNextStep:
            controller.nextStep()

        if controller.step == 5:
            predictor = Predictor()

            value = predictor.predict(player)
            converter = Converter()
            strValue = converter.convertStringValue(value)

            textos.clear()
            textos.append("O seu jogador vale aproximadamente " + strValue)
            textos.append("Então, quer que eu veja mais um jogador? Neste caso, qual é o overall dele?")

            for texto in textos:
                bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
                time.sleep(2)
                bot.send_message(chat_id=update.message.chat_id, text=texto, parse_mode=telegram.ParseMode.HTML, action = telegram.ChatAction.TYPING)
                
            controller.step = 1

    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)

    if(env == 'production'):
        PORT = int(os.environ.get('PORT', '5000'))
        HEROKU_APP = os.environ.get('HEROKU_APP')
        logger.info("PORT: " + str(PORT))
        logger.info("HEROKU_APP: " + HEROKU_APP)
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
        updater.bot.set_webhook("https://"+ HEROKU_APP +".herokuapp.com/" + TOKEN)
        updater.idle()
    else:
        updater.start_polling()
except Exception as e:
    print(e)

        