from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foods/', include('foods.urls')),
    path('greetings/', include('greetings.urls')),
    path('menus/', include('menus.urls')),
]