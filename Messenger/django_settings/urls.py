from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('log_auth.urls')),
    path('twitter_app/', include('twitter_app.urls')),
    path('todo_app/', include('todo_app.urls')),
]
