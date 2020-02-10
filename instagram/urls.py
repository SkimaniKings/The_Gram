from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url('login/', views.login, name='login'),
    url(r'profile/', views.profile, name='profile'),
    url('home_page/', views.home_page, name='home_page'),
      
]
