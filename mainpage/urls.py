from django.urls import path
from mainpage.views.home import index
urlpatterns = [
            path('',index),
]
