import telebot
import conf
import markovify
from flask import Flask, request
import os


WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT) #тут у нас по сути конструктор хероку ссылки: хост - то что хероку дает в качестве ссылки(это делается под конец)
WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN) #здесь конф.токен - мы справшиваем наш токен из файла конф
#в конце конспекта хероку есть как протолкнуть токен в винду и в хероку - так правильнее, мой код издевательство
telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'} #задаем прокси чтобы обойти блокировку тг - для этого нужно загрузить еще пару модулей - записаны в файле requirements
bot = telebot.TeleBot(conf.TOKEN, threaded=False) #это наш бот с токеном вызывается

bot.remove_webhook() #просто важная строчка чтобы хук работал
bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH) #делаем магию удаленного доступа к боту через хероку, в конспектк есть как приделать это без моих ебнутых переменных.

server = Flask(__name__) #вот и наш сервак на фласке в конспектах зовется app, a не server (везде дальше в файле тоже)


def sent_builder(): #хоба, вот функция для цепи
    with open('War_Peace.txt', encoding='utf-8') as f: #открываем войну и мир
        train = f.read() #читаем войну и мир в переменную
    m = markovify.Text(train) #хоп, тренируем цепь на тексе
    return m.make_short_sentence(max_chars=200) #генерим предложение в макс 200 символов длиной и отдаем его


@bot.message_handler(commands=['start', 'help']) #команды бота пошли - эта говорит ему вот так отвечать на /start или /help
def send_welcome(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Это бот, генерирующий свою "Войну и мир"\nОт вас требуется ввести любое сообщение')

@bot.message_handler(func=lambda m: True) #вот так мы отвечаем на последующее абсолюьно любое соо
def my_function(message):
    bot.send_message(message.chat.id, 'Толстой написал:\n{} '.format(sent_builder())) #вот и наша функция цепочки (вставляется в {}- thats how .format works, you can
#also do smth like: (message.chat.id, 'Толстой написал:\n', sent_builder())

@server.route('/' + conf.TOKEN, methods=['POST']) #thats flask - tells our server to get messages from our bot - лучше найти ту же хуйню в шаблоне в статье по хероку, просто вставить туда токен
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/") #тоже фласк цеплялка, надо вствить свою ссылку в урл - тоже лучше найти в шаблоне ибо я хз откуда брал это - там она app.route()
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://rocky-stream-47814.herokuapp.com/' + conf.TOKEN)
    return "!", 200

if __name__ == '__main__': #вот эта хуйня говорит серверу запускаться
    import os

    server.debug = True
    port = int(os.environ.get("PORT", 5000))
    server.run(host='0.0.0.0', port=port)

#профит