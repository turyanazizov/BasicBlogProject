from django.urls import path
from blog.views import blog,single_post

app_name='blog'

urlpatterns = [
    path('', blog,name='blog'),
    path('<str:name>',single_post,name='single-post')
]