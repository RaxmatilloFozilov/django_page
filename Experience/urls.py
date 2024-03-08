from django.urls import path
from .views import Sarlavha,index
urlpatterns = [
    path('',index,name='index'),
    path('',Sarlavha),
]