from django.urls import path
from . import views

urlpatterns = [

    # path('', views.index, name='home'),
    path('<int:year>/<str:month>/', views.index, name='home'),

]


