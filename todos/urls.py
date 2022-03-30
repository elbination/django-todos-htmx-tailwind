from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-task/', views.add_task, name='add_task'),
    path('update-task/<int:pk>/', views.update_task, name='update_task'),
    path('delete-task/<int:pk>/', views.delete_task, name='delete_task'),
    path('edit-task/<int:pk>/', views.edit_task, name='edit_task'),

]
