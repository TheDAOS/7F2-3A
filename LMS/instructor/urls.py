from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.instructor_dashboard, name='instructor_dashboard'),
    path('upload/', views.upload_file, name='upload_file'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)