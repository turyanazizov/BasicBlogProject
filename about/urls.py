from django.urls import path
from about.views import about,single_project

app_name='about'

urlpatterns = [
    path('', about,name='about'),
    path('project/', single_project,name='single-project'),
]