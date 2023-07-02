from django.shortcuts import render
from .models import Post
# Create your views here.

from django.http import HttpResponse

# posts=[
#     {
#         'author':'Destiny Franks',
#         'title':'Blog Posts',
#         'content':'This is my first Blog post',
#         'date_posted':'7th August 2021'
#     },
#     {
#         'author':'jane doe',
#         'title':'Blog Post 2',
#         'contest':'This is my second blog post',
#         'date_posted':'14th August 2021'
#     }
# ]
def home(request):
    context={
        'posts':Post.objects.all()
    }
    # return HttpResponse("<h1>hello</h1>")
    return render(request,"blog/home.html",context)

def about(request):
    # return HttpResponse("<h1>hello</h1>")
    return render(request,"blog/about.html")


# def about(request):
#     render(request)