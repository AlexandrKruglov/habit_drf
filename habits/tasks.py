from habits.models import Habit
import datetime
from celery import shared_task

from habits.services import send_telegram_message


@shared_task(name="habits.tasks.send_tg_message")
def send_tg_message():
    habits = Habit.objects.filter(is_pleasant=False)
    print("ok")
    for habit in habits:
        message = f'не забудте выполнить {habit.action}'
        if habit.period == 'ежедневно':
            if habit.last_remind < datetime.date.today():
                if habit.time <= datetime.datetime.now().time():
                    chat_id = habit.user.telegram_id
                    if chat_id:
                        send_telegram_message(telegram_id=chat_id, message=message)
                        habit.last_remind = datetime.date.today()
                        habit.save()
        elif habit.period == 'через день':
            if habit.last_remind + datetime.timedelta(days=1) < datetime.date.today():
                if habit.time <= datetime.datetime.now().time():
                    chat_id = habit.user.telegram_id
                    if chat_id:
                        send_telegram_message(telegram_id=chat_id, message=message)
                        habit.last_remind = datetime.date.today()
                        habit.save()
        elif habit.period == 'через три дня':
            if habit.last_remind + datetime.timedelta(days=3) < datetime.date.today():
                if habit.time <= datetime.datetime.now().time():
                    chat_id = habit.user.telegram_id
                    if chat_id:
                        send_telegram_message(telegram_id=chat_id, message=message)
                        habit.last_remind = datetime.date.today()
                        habit.save()
        elif habit.period == 'раз в неделю':
            if habit.last_remind + datetime.timedelta(days=7) < datetime.date.today():
                if habit.time <= datetime.datetime.now().time():
                    chat_id = habit.user.telegram_id
                    if chat_id:
                        send_telegram_message(telegram_id=chat_id, message=message)
                        habit.last_remind = datetime.date.today()
                        habit.save()
