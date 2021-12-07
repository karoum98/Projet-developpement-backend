from django.urls import path
from . import views


urlpatterns=[
    path('',views.analyse_sentimentalAPI, name='analyse_sentimentalAPI'),
]