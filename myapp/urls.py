from django.urls import path
from . import views

urlpatterns = [

    path('', views.base, name='base'),
    path('<int:year>/<str:month>/', views.index, name='home'),
    path('testing/', views.testing, name= 'testing'),

]


