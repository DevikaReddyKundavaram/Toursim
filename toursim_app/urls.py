from django.urls import path
from .views import index, state,city,location

urlpatterns = [
    path('', index, name='index'),
    path('state', state, name='state'),
    path('state/<str:state_name>/', state, name='state_detail'),
    path('city',city,name='city'),
    path('city/<str:city_name>/',city,name='city'),
    path('location',location,name='location'),
    path('location/<str:location_name>/',location,name='location'),


]