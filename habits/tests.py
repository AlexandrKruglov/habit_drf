from datetime import timedelta
from rest_framework import status

from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестируем привычки."""

    def setUp(self):
        self.user = User.objects.create(email="admin@mail.ru")

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place="тест место",
            time="14:00:00",
            action="сделать тест",
            is_pleasant=False,
            pleasant_habit=None,
            time_to_complete=timedelta(seconds=120),
            is_public=True,
            reward="тест возношграждение",
        )

    def test_habit_list(self):
        """Тестируем вывод списка привычек."""

        response = self.client.get('/habits/habit/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)

    def test_habit_create(self):
        """Тестируем создание привычки."""
        data = {
            "action": "test_create",
            "time_to_complete": 120,
        }
        response = self.client.post('/habits/habit/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        """Тестируем изменение привычки."""
        data = {
            "reward": "награда",
        }
        response = self.client.patch('/habits/habit/1/', data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("reward"), "награда")

    def test_habit_delete(self):
        """Тестируем удаление привычки."""

        response = self.client.delete("/habits/habit/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)
