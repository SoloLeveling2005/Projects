from django.contrib import admin
from django.urls import path
from django_app import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'django_app'
urlpatterns = [
    path('', views.index, name='index'),

    # path('delete_tweet/<int:tweet_id>/', views.delete_tweet, name='delete_tweet'),


]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)