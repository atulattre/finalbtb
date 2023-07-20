from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   
    path('',views.loginpage,name='loginpage'),
    path('homepage',views.homepage,name='homepage'),
    path('signuppage',views.signuppage,name='signuppage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('cp',views.cp,name='cp'),
    path('all_flat',views.all_flat,name='all_flat'),#cp=complete profile
    path('contact/<int:id>/',views.contact,name='contact'),


   
   
  
   



    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)