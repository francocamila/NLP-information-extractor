from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_pdf, name='upload_pdf'),
    path('list_keywords', views.list_keywords, name='list_keywords')
]