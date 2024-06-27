from django.shortcuts import render


# Create your views here.
def posts_list(request):
    return render(request, "posts/posts_list.html")      # first accessing the posts namespace in the templates and then the html
