from django.urls import path
from . import views

urlpatterns = [
    path('', views.instructor_dashboard, name='instructor_dashboard'),
    path('upload/', views.upload_file, name='upload_file'),
]