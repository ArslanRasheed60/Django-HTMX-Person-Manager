from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('person_list/', views.person_list, name='person_list')
]