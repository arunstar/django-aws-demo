from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

@api_view()
def hello(request):
    print(request.data)
    return Response("Hello")


class UserSerializer(serializers.Serializer):
    pass