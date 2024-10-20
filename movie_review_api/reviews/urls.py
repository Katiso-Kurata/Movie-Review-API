from django.urls import path
from . import views
from .views import UserListCreateView, UserDetailView, ReviewListCreateView, ReviewDetailView



urlpatterns = [
    
    
    path('users/', views.UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('reviews/', views.ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),

]
