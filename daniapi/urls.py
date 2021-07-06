from django.urls import path
from .views import endpoints, getallposts, getpost, getalltags, gettag, postbytag

urlpatterns = [
    path('', endpoints),
    path('posts/', getallposts),
    path('post/<str:id>/', getpost),
    path('tags/', getalltags),
    path('tag/<str:id>', gettag),
    path('postbytag/<str:id>', postbytag),
]