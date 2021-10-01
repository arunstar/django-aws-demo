from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from .models import Products, User
from .serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status

import random

class ProductViewSet(viewsets.ModelViewSet):

    def list(self,request): # /api/products 
        products = Products.objects.all()
        serialzer = ProductSerializer(products,many=True)
        return Response(serialzer.data)

    def create(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status.HTTP_201_CREATED)



    def retrieve(seld,requests,pk=None):
        product = Products.objects.get(id=pk)
        serializers = ProductSerializer(product)
        return Response(serializers.data)



    def update(seld,requests,pk=None):
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(instance=product,data=requests.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status.HTTP_202_ACCEPTED)

    def destroy(seld,requests,pk=None):
        product = Products.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    def get(self,request):
        users = User.objects.all()
        print(users)
        user = random.choice(users)
        return Response({
            'id':user.id,
            # 'name' : user.name
        })

