from django.db import models
import datetime

from users.models import User

# Create your models here.
NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    DAILY = 'ежедневно'
    EVERY_OTHER_DAY = 'через день'
    EVERY_THIRD_DAY = 'через три дня'
    WEEKLY = 'раз в неделю'

    CHOICE_PERIOD = [
        (DAILY, 'ежедневно'),
        (EVERY_OTHER_DAY, 'через день'),
        (EVERY_THIRD_DAY, 'через три дня'),
        (WEEKLY, 'раз в неделю'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='пользователь')
    place = models.CharField(max_length=200, **NULLABLE, verbose_name='место привычки')
    time = models.TimeField(default=datetime.time(11, 00), verbose_name='время привычки')
    action = models.CharField(max_length=200, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='приятная привычка?')
    period = models.CharField(
        max_length=100,
        choices=CHOICE_PERIOD,
        default=DAILY,
        verbose_name="Периодичность")
    pleasant_habit = models.ManyToManyField('self', **NULLABLE, symmetrical=False,
                                            limit_choices_to={'is_pleasant': True})
    reward = models.CharField(max_length=200, **NULLABLE, verbose_name='вознограждение')
    time_to_complete = models.PositiveIntegerField(verbose_name='время на выполнение привычки в секундах')
    is_public = models.BooleanField(default=False, verbose_name='сделать публичной?')
    time_started = models.DateTimeField(auto_now_add=True)
    last_remind = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
