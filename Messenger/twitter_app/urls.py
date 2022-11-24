from django.contrib import admin
from django.urls import path
from twitter_app import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'twitter_app'
urlpatterns = [
    # Глобальные пути
    path('', views.log_auth, name='log_auth'),  # страница с регистрацией
    path('home/', views.home, name='home'),  # главная страница
    # path('explore/', views.explore, name='explore'),  # страница с поиском
    # path('<str:nickname>/', views.profile, name='profile'),  # страница профиля пользователя (любого)
    # path('<str:nickname>/status/<int:id_tweet>', views.status_tweet, name='status_tweet'),  # страница просмотра твита


    # path('<int:user_id>/<int:id_tweet>/', views.check_tweet, name='check_tweet'),
    path('new_tweet/', views.new_tweet, name='new_tweet'),
    # path('home/<int:code>/get_info_new_tweet/', views.get_info_new_tweet, name='get_info_new_tweet'),
    # path('home/<int:id_tweet>/<int:user_id>/like_tweet/<int:parent_id_tweet>/<int:parent_user_id>',
    #      views.like_tweet,
    #      name='like_tweet'),
    # path('home/<int:id_user>/<int:id_tweet>/delete_tweet/', views.delete_tweet, name='delete_tweet'),
    # path('get_info_tweet/', views.get_info_tweet, name='get_info_tweet'),
    # path('home/<int:code>/', views.home, name='home'),
    # path('my_api_one/<int:post_id>/', views.my_api_one),
    # path('my_api/', views.my_api),

    # path('check_user/<int:user_id>', views.check_user, name='check_user'),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
