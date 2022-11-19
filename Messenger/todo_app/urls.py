from django.contrib import admin
from django.urls import path
from todo_app import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'todo_app'
urlpatterns = [
    # Главная страница с регистрацией и авторизацией
    path('', views.home),
    path('home/<int:user_id>/', views.home, name='home'),
    path('home/<int:user_id>/new_task', views.new_task, name='new_task'),
    path('home/<int:task_id>/complete_task', views.complete_task, name='complete_task'),
    path('home/<int:task_id>/delete_task', views.delete_task, name='delete_task'),
    path('home/<int:task_id>/task_detail', views.task_detail, name='task_detail'),
    # path('my_api_one/<int:post_id>/', views.my_api_one),
    # path('my_api/', views.my_api),
    path('get_example_tasks/', views.get_example_tasks),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
