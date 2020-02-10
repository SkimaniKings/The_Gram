from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url('login/', views.login, name='login'),
    url('profile/', views.profile, name='profile'),
    #   url('search/', views.search_results, name='search_results'),
    
]
