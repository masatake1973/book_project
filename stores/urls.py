from django.urls  import path
from . import views

app_name = 'stores'
urlpatterns = [
    path('', views.store_list, name='store_list'),
    path('<int:store_id>/', views.store_detail, name='store_detail'),
]