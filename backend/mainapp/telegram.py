import telegram
from .models import Users
from django.conf import settings
import asyncio


def send_message():
    await asyncio.sleep(1)
    form = Users.objects.latest('time_register')
    dict_form = form.__dict__
    del dict_form['_state']
    message = f"Бронь пришла с сайта\n" \
              f"ФИО: {dict_form['name']}\n" \
              f"Время: {dict_form['time']}\n" \
              f"Дата: {dict_form['date']}\n" \
              f"Кол-во гостей: {dict_form['people_number']}\n" \
              f"Номер телефона: {dict_form['phone_number']}\n" \
              f"Комментарий: {dict_form['comment']}"
    try:
        bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
        bot.send_message(chat_id=settings.CHAT_ID, text=message)
        return True
    except Exception as e:
        print(f"Ошибка отправки сообщения: {e}")
        return False

