from django.contrib import admin
from django.urls import path
from twitter_app import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'twitter_app'
urlpatterns = [
    # Главная страница с регистрацией и авторизацией
    path('', views.home),
    path('<int:id_tweet>/', views.home),
    path('home/', views.home),
    # path('home/<int:code>/new_tweet/', views.new_tweet, name='new_tweet'),
    path('new_tweet/', views.new_tweet, name='new_tweet'),
    path('home/<int:code>/get_info_new_tweet/', views.get_info_new_tweet, name='get_info_new_tweet'),
    path('home/<int:id_tweet>/<int:user_id>/like_tweet/', views.like_tweet, name='like_tweet'),
    path('home/<int:id_user>/<int:id_tweet>/delete_tweet/', views.delete_tweet, name='delete_tweet'),
    path('get_info_tweet/', views.get_info_tweet, name='get_info_tweet'),
    path('home/<int:code>/', views.home, name='home'),
    # path('my_api_one/<int:post_id>/', views.my_api_one),
    # path('my_api/', views.my_api),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
