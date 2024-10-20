# reviews/views.py

from rest_framework import generics
from .models import User, Review
from .serializers import ReviewSerializer, UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


    def get_queryset(self):
        # Only return reviews created by the authenticated user or the review itself
        user = self.request.user
        return Review.objects.filter(user=user) | Review.objects.filter(id=self.kwargs['pk'])


