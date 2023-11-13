from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'custom_user'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/', views.DetailView.as_view(), name='detail'),
]