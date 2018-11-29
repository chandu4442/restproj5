from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from .serializers import ProductSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
def input(request):
    return render(request,'input.html')
def display(request):
    recs=Product.objects.all()
    return render(request,'display.html',{'records':recs})
class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#class ProductList(generics.ListAPIView):
 #   queryset = Product.objects.all()
  #  serializer_class = ProductSerializer

