from django.urls import path
from . import views

app_name = 'company'
urlpatterns = [
    path('company/create/', views.CreateView.as_view(), name='create'),
    path('company/list/', views.ListView.as_view(), name='list'),
    path('company/detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
]