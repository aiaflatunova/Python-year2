import telebot
import conf
import markovify
from flask import Flask, request
import os


WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN)

telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}
bot = telebot.TeleBot(conf.TOKEN, threaded=False)

bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)

server = Flask(__name__)


def sent_builder():
    with open('War_Peace.txt', encoding='utf-8') as f:
        train = f.read()
    m = markovify.Text(train)
    return m.make_short_sentence(max_chars=200)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Это бот, генерирующий свою "Войну и мир"\nОт вас требуется ввести любое сообщение')

@bot.message_handler(func=lambda m: True)
def my_function(message):
    bot.send_message(message.chat.id, 'Толстой написал:\n{} '.format(sent_builder()))

@server.route('/' + conf.TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://rocky-stream-47814.herokuapp.com/' + conf.TOKEN)
    return "!", 200

if __name__ == '__main__':
    import os

    server.debug = True
    port = int(os.environ.get("PORT", 5000))
    server.run(host='0.0.0.0', port=port)


