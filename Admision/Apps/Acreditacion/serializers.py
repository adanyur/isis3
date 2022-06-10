from rest_framework import serializers
from .models import *


class AcreditacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acreditacion
        fields ='__all__'