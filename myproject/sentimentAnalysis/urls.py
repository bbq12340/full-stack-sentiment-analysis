from django.contrib import admin
from django.urls import path

from . import views

app_name = 'sentimentAnalysis'

urlpatterns = [
    path('', views.InputTextView.as_view(), name='index'),
    path('predict/', views.predict, name='predict')
]
