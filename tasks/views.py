from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serilaizers import TaskSerializer
from django.contrib.auth.models import User


# API to create a task
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # create a new task
    def create(self, request):
        data = request.data
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def assign_task(self, request, pk):
        # Check if the task exists
        try:
            task = self.get_object()
        except ObjectDoesNotExist:
            return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Get the user IDs from the request data
        user_ids = request.data.get('user_ids', [])

        # If no user IDs are provided, return an error
        if not user_ids:
            return Response({'error': 'No user IDs provided.'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate each user ID
        valid_users = User.objects.filter(id__in=user_ids)
        invalid_ids = set(user_ids) - set(valid_users.values_list('id', flat=True))

        if invalid_ids:
            return Response({'error': f'Invalid user IDs: {list(invalid_ids)}'}, status=status.HTTP_400_BAD_REQUEST)

        # Assign valid users to the task
        task.assigned_users.add(*valid_users)
        task.save()

        return Response({'status': 'Task assigned successfully to users.',
                         'assigned_user_ids': list(valid_users.values_list('id', flat=True))},
                        status=status.HTTP_200_OK)

    # API to get tasks for a specific user
    def list_user_tasks(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        tasks = Task.objects.filter(assigned_users=user)
        serialized_tasks = []

        # Remove 'assigned_users' field from each task
        for task in tasks:
            task_data = TaskSerializer(task).data
            task_data.pop('assigned_users', None)  # Remove the 'assigned_users' field
            serialized_tasks.append(task_data)

        return Response(serialized_tasks)
