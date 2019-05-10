from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from . import models
from . import serializers
# Create your views here.

class CarViewSet(viewsets.ModelViewSet):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer


class ShowroomViewSet(viewsets.ModelViewSet):
    queryset = models.Showroom.objects.all()
    serializer_class = serializers.ShowroomSerializer


class ManufactureViewSet(viewsets.ModelViewSet):
    queryset = models.Manufactor.objects.all()
    serializer_class = serializers.ManufactureSerializer

    # def create(self, *args, **kwargs):
    #     serializers.ManufactureSerializer()
    #     print(self.request.data)
    #     return Response(data={})


class ManufactorModelViewSet(viewsets.ModelViewSet):
    queryset = models.ManufactorModel.objects.all()
    serializer_class = serializers.ManufactorModelSerializer