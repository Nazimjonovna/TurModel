from rest_framework import serializers
from .models import *

class Turserializer(serializers.ModelSerializer):
    class Meta():
        model = TurModel
        fields = '__all__'