from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url('profile/', views.profile, name='profile'),
    url('home_page/', views.home_page, name='home_page'),
    url('update/',views.update, name='update'),
    url('post_image/',views.post_image, name='post_image'),
  
    
      
]
