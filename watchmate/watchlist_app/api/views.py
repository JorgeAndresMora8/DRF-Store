from django.shortcuts import render
from watchlist_app.models import Shoes, Category, Review
from django.http import JsonResponse
from watchlist_app.api.serializer import ShoeSerializer, CategorySerializer, ReviewSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics
from rest_framework.views import APIView

class CreateReview(generics.CreateAPIView): 
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        shoe = Shoes.objects.get(id=pk)
        
        serializer.save(shoes=shoe)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
class ReviewList(generics.ListAPIView): 
    serializer_class = ReviewSerializer
    
    def get_queryset(self): 
        pk = self.kwargs['pk']
        return Review.objects.filter(shoes=pk)  


class CategoryListAV(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 

class CategoryDetailAV(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
        
class ProductListAV(generics.ListCreateAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoeSerializer
    
    def get(self, request, *args, **kwargs): 
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs): 
        return self.create(request, *args, **kwargs)


class ProductDetailAV(generics.RetrieveUpdateDestroyAPIView): 
    
    queryset = Shoes.objects.all()
    serializer_class = ShoeSerializer
      
    