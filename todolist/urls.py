from django.contrib import admin
from django.urls import path,include # import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Todo/',include('todoapp.urls'))  # add this line
]