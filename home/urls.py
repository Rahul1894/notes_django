from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from . import views
urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('authorized',views.authorizedView.as_view()),
    path('login',views.LoginInterfaceView.as_view(),name='login'),
    path('logout',views.LogoutInterfaceView.as_view(),name='logout'),
    path('signup',views.Signupview.as_view(),name='signup')
]