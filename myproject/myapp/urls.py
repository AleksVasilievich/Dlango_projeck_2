from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.first, name='first'),
    path('about/', views.about, name='about'),
]