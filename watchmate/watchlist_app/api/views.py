from django.shortcuts import render
from watchlist_app.models import Shoes, Category
from django.http import JsonResponse
from watchlist_app.api.serializer import ShoeSerializer, CategorySerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


class CategoryListAV(APIView):
    
    def get(self, request):
        categoryList = Category.objects.all()
        serializer = CategorySerializer(categoryList, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else: 
            return Response(serializer.errors, status=400)
        
        
class CategoryDetailAV(APIView):
    
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        category = self.get_object(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        instance = self.get_object(pk=pk)
        serializer = CategorySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try: 
            Category.objects.get(pk=pk).delete()
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

class ProductListAV(APIView):

    def get(self, request):
        product_list = Shoes.objects.all()
        serializer = ShoeSerializer(product_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShoeSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=201)
        else: 
            return Response(serializer.errors, status=400)

        
        
class ProductDetailAV(APIView): 
    
    def get_object(self, pk):
        try:
            return Shoes.objects.get(pk=pk)
        except Shoes.DoesNotExist: 
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        product = self.get_object(pk=pk)
        serializer = ShoeSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
    def put(self, request, pk):
        instance = self.get_object(pk=pk)
        serializer = ShoeSerializer(instance, data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        product = self.get_object(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    