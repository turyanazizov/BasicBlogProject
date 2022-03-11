from django.urls import path
from blog.views import blog,single_post

app_name='blog'

urlpatterns = [
    path('', blog,name='blog'),
    path('post/',single_post,name='single-post')
]