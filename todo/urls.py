from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_list),  # Route for GET and POST
]
