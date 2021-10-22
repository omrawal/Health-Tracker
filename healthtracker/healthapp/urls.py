from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('register', views.registerPage, name='register'),
    path('progress', views.progressPage, name='progress'),
    path('addstats', views.addStatsPage, name='addstats'),
]
