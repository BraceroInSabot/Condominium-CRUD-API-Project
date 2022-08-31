from rest_framework import serializers
from core.models import NameModel, CNPJModel, CondominiumInfoModel


class NameSerializer(serializers.ModelSerializer):
    CNPJ = serializers.StringRelatedField()
    class Meta:
        model = NameModel
        fields = ("id", "name", "CNPJ")


class CNPJSerializer(serializers.ModelSerializer):

    class Meta:
        model = CNPJModel
        fields = '__all__'


class CondominiumInfoSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()
    CNPJ = serializers.StringRelatedField()

    class Meta:
        model = CondominiumInfoModel
        fields = ("id", 'name', 'CNPJ', "owner", 'address', 'email')