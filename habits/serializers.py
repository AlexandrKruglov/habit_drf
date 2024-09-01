from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import PleasantValidator


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [PleasantValidator(is_pleasant='is_pleasant', pleasant_habit='pleasant_habit', reward='reward', time_to_complete='time_to_complete')]
