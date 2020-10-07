import datetime
from datetime import datetime
import telebot
import config

bot = telebot.TeleBot(config.token);


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     "Здарова заводчанин, <b>{0.first_name}!</b>\nКогда ты пришел на завод?".format(
                         message.from_user,
                         bot.get_me()),
                     parse_mode='html')
    bot.send_message(message.chat.id, "Например 28/11/2019")


@bot.message_handler(content_types=['text'])
def get_date(message):
    date_of_work = message.text
    now = datetime.now()
    now.toordinal()
    try:
        valid_date = datetime.strptime(date_of_work, '%d/%m/%Y')
        valid_date.toordinal()
        a = 1
        if valid_date > datetime.now():
            bot.send_message(message.chat.id, 'Ты кого наебать решил, пес?')
            bot.send_message(message.chat.id, 'А?')
            bot.send_message(message.chat.id, 'Введи нормально дату, заебал')
            bot.send_message(message.chat.id, "Например 28/11/2019")
            a = 0
    except ValueError:
        bot.send_message(message.chat.id, 'Введи нормально дату, дегрод')
        bot.send_message(message.chat.id, "Например 28/11/2019")
        a = 0
    if a == 1:

        days_all = now - valid_date
        print(days_all.days)
        if days_all.days % 10 == 1 and days_all.days % 100 != 11:
            day_name = (" день")
        elif 2 <= days_all.days % 10 <= 4 and (days_all.days % 100 < 10 or days_all.days % 100 >= 20):
            day_name = (" дня")
        else:
            day_name = (" дней")
        bot.send_message(message.chat.id, "Ты деградируешь на заводе уже " + str(days_all.days) + str(day_name))


bot.polling(none_stop=True, interval=0)

