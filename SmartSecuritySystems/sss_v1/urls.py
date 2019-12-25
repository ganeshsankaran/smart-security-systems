from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('features', views.features, name='features'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('portal', views.portal, name='portal'),
    path('register', views.register, name='register'),
    path('search', views.search, name='search'),
    path('upload', views.upload, name='upload'),
]

