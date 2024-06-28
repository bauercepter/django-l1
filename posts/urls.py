# Created this file manually for posts app

from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path(
        "", views.posts_list, name="list"
    ),  # views functions are added as higher-order functions
    path(
        "<slug:slug>", views.post_page, name="page"
    ),  # using slug path converter and the pattern is -> pathConverter:slug where both are named slug in this case
]


# also need to register these new urls to the main urls.py file
