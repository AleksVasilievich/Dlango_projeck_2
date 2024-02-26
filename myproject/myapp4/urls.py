from django.urls import path
from .views import form_app4, upload_image



urlpatterns = [
    path('add/', form_app4, name='user_form'),
    path('add/upload/', upload_image, name='upload_image'),
]