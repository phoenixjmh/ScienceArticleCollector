
from . import views

from django.urls import path


urlpatterns = [
    
    path('',views.index, name='index'),

    path('collect/', views.collect, name = 'collect')
]
