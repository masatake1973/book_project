# users/urls.py

from django.urls import path
from . import views

app_name = 'users' # アプリケーションのURL名前空間を定義
urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('<str:username>/', views.user_detail, name='user_detail'), # 個々のユーザーページ
]