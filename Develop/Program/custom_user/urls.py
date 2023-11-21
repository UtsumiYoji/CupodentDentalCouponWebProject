from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'custom_user'
urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/', views.UserDetailView.as_view(), name='detail'),
    path('update/', views.UserUpdateView.as_view(), name='update'),
    path('company/create/', views.CompanyCreateView.as_view(), name='company_create'),
    path('company/list/', views.CompanyListView.as_view(), name='company_list'),
    path('company/detail/<int:pk>/', views.CompanyDetailView.as_view(), name='company_detail'),
]