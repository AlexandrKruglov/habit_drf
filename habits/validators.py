from rest_framework.serializers import ValidationError


class PleasantValidator:
    def __init__(self, is_pleasant, pleasant_habit, reward, time_to_complete):
        self.is_pleasant = is_pleasant
        self.pleasant_habit = pleasant_habit
        self.reward = reward
        self.time_to_complete = time_to_complete

    def __call__(self,value):
        temp_is_pleasant = dict(value).get(self.is_pleasant)
        temp_pleasant_habit = dict(value).get(self.pleasant_habit)
        temp_reward = dict(value).get(self.reward)
        temp_time_to_complete = dict(value).get(self.time_to_complete)
        print(temp_time_to_complete)
        if temp_is_pleasant:
            if temp_pleasant_habit is not None:
                raise ValidationError(f'{self.pleasant_habit} это поле не заполняеся т.к. это приятная привычка')
            if temp_reward is not None:
                raise ValidationError(f'{self.reward} это поле не заполняеся т.к. это приятная привычка')
        else:
            if temp_pleasant_habit:
                if temp_reward is not None:
                    raise ValidationError(f'{self.reward} это поле не заполняеся т.к. к уже есть приятная привычка')
            if temp_reward:
                if temp_pleasant_habit is not None:
                    raise ValidationError(f'{self.pleasant_habit} это поле не заполняеся т.к. уже есть вознагрождение')
        if int(temp_time_to_complete) > 120:
            raise ValidationError(f'{self.time_to_complete} время на выполнение привычки не может превышать 120 секунд')
        return value
