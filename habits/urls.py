from django.urls import path
from rest_framework.routers import SimpleRouter

from habits.apps import HabitsConfig
from habits.views import HabitViewSet

app_name = HabitsConfig.name


router = SimpleRouter()
router.register(r'habit', HabitViewSet, basename='habit')

urlpatterns = []
urlpatterns += router.urls

