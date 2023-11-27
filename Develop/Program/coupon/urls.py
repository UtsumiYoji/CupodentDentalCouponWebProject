from django.urls import path
from . import views

app_name = 'coupon'
urlpatterns = [
    path('', views.CouponListView.as_view(), name='list'),
    path('create/', views.CouponCreateView.as_view(), name='create'),
    path('create/image/', views.CouponImageCreateView.as_view(), name='image_create'),
    path('detail/<int:pk>/', views.CouponDetailView.as_view(), name='detail'),
    path('cart/', views.CartListView.as_view(), name='cart'),
]