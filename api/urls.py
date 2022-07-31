from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-rockets', views.get_all_rockets, name='get_all_rockets'),
    path('rocket-details/<str:pk>', views.get_rocket_details, name='get_rocket_details'),
]
