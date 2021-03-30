from django.urls import path
from . import views

app_name = 'img2txt'

urlpatterns = [
    path('', views.index, name='index'),
    path('extract/', views.ExtractText.as_view(), name='extract_text'),
]

