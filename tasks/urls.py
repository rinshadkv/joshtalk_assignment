from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/<int:pk>/assign', TaskViewSet.as_view({'post': 'assign_task'})),
    path('users/<int:user_id>/tasks', TaskViewSet.as_view({'get': 'list_user_tasks'})),
]
