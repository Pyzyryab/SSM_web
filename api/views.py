from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
# def main(request):
#     return HttpResponse('<H1>Hello</H1>')

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer