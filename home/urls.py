from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api-gen'   , views.api_generator, name='api_generator'),
    path('dyn-datatb', views.dyn_datatb   , name='dyn_datatb'   ),
]
