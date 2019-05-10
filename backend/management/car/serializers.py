from rest_framework import serializers

from . import models

class ManufactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufactor
        fields = '__all__'


class ManufactorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ManufactorModel
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car
        fields = '__all__'



class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Showroom
        fields = '__all__'
