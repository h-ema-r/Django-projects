from django.urls import path
from . import views

urlpatterns = [
    path('malaria_classification/', views.malaria_classification, name='malaria_classification'),
]
