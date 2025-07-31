from django.urls import path
from . import views

app_name = 'core' # アプリケーションのURL名前空間を定義
urlpatterns = [
    path('', views.index, name='index'), # トップページ
]