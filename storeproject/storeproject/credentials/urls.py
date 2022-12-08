from . import views
from django.urls import path

urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('base',views.base,name='base'),
    path('one',views.one,name='one'),
    path('new',views.new,name='new')
]