from django.urls import path
from todoapp import views

urlpatterns = [
    path('index/',views.index),
    path("update/<int:pk>/", views.update_task,),
    path("delete/<int:pk>/", views.delete_task,),
]