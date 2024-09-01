from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginators import CustomPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        return habit.save()

    def get_permissions(self):
        if self.action in ['update', 'retrieve']:
            self.permission_classes = (IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (IsOwner,)
        return super().get_permissions()

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        queryset_2 = self.queryset.filter(is_public=True)
        queryset = queryset | queryset_2
        return queryset
