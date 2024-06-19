from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import BookingSerializer,MenuSerializer,UserSerializer
from .models import *
from rest_framework import generics 
from rest_framework.permissions import IsAuthenticated
# Create your views here.

""" class MenuView(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items,many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MenuSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data}) """

class UserViewSet(viewsets.ModelViewSet):
    permission_classes= [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})
