from rest_framework import serializers
from .models import ServiciosExternos


class ServiciosExternosSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiciosExternos
        fields = "__all__"
