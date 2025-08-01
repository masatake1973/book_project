# books/urls.py

from django.urls import path
from . import views

app_name = 'books' # アプリケーションのURL名前空間を定義
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:book_id>/', views.book_detail, name='book_detail'), # 個々の本のページ
]