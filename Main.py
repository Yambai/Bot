import telebot
from random import random
oneZero =[str(i) for i in range(101)]
rand_m=0.4
from  markov2 import *
bot = telebot.TeleBot('5460412943:AAEAkucQwE-ir2wBDco9HOIZ8dPD7g0wFUc')
@bot.message_handler(commands=["rand"])
def test(message):
     bot.reply_to(message, 'Введите вероятность')
     @bot.message_handler(content_types=['text'])
     def message_input_step(message):
     	global rand, rand_m
     	rand = message.text
     	if rand in oneZero:
     		bot.reply_to(message, f'Ваш текст: {message.text}')
     		rand_m = int(rand)/100
     	else:
     		bot.reply_to(message, f'{message.text} это не число от 0 до 100')
     		
     bot.register_next_step_handler(message, message_input_step)
	
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отвчаю только на текст, тестовый челик я )')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    rand_ooo=random()
    if rand_ooo<=rand_m:
    	ooo=markovf(message.text)
    else:
    	ooo=None
    if ooo==None:
        print('Новое слово')
    else:
        bot.send_message(message.chat.id,ooo)

bot.polling(none_stop=True, interval=0)

