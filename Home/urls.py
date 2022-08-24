from django.urls import path
from Home import views
from django.conf import settings
from django.conf.urls.static import static

from .views import  *

urlpatterns = [
    path('', views.home ,name="home"),
    path('contact', views.contact ,name="contact"),
    path('testimonial', views.testimonial ,name="testimonial"),
     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)