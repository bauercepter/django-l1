# Created this file manually for posts app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list)          # views functions are added as higher-order functions
]


# also need to register these new urls to the main urls.py file