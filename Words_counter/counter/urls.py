from django.urls import path
from . import views

app_name = 'counter'

urlpatterns = [
    # представления поста
    path('', views.upload_file, name='upload_file'),
]
