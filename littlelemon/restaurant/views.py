from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookingSerializer,MenuSerializer
from .models import *
# Create your views here.

class MenuView(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items,many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MenuSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})
        