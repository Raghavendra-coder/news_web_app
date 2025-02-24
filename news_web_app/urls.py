from . import views
from django.urls import path

urlpatterns = [
    path('get_latest_news/', views.GetLatestNewsAPI),
    path('index', views.t_view),
    path('automated_call', views.automated_call, name='automated_call'),
    path('sample/', views.sample, name='sample'),
    path('get_task_status/<task_id>/', views.get_task_status, name='get_task_status'),
]