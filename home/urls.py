from django.urls import path
from home.views import home,single_project

app_name='home'

urlpatterns = [
    path('', home,name='home'),
    path('<str:name>', single_project,name='single-project'),
]