from django.contrib import admin
from django.urls import path
from todo_app import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'todo_app'
urlpatterns = [
    # Главная страница с регистрацией и авторизацией
    # path('', views.home),
    # path('home/<int:user_id>/', views.home, name='home'),
    # path('home/<int:user_id>/new_task', views.new_task, name='new_task'),
    path('complete_task/<task_id>/', views.complete_task, name='complete_task'),
    path('delete_task/<task_id>', views.delete_task, name='delete_task'),
    # path('home/<int:task_id>/task_detail', views.task_detail, name='task_detail'),
    # # path('my_api_one/<int:post_id>/', views.my_api_one),
    # # path('my_api/', views.my_api),
    # path('get_example_tasks/', views.get_example_tasks),
    path('create_task/<text>', views.create_task, name='create_task'),
    path('get_tasks/', views.get_tasks, name='get_tasks'),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
