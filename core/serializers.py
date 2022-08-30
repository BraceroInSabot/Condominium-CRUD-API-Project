from dataclasses import field
from rest_framework import serializers
from core.models import NameModel, CNPJModel, BuildRegisterModel, BuildInfoModel


class NameSerializer(serializers.ModelSerializer):

    class Meta:
        model = NameModel
        fields = '__all__'


class CNPJSerializer(serializers.ModelSerializer):

    class Meta:
        model = CNPJModel
        fields = '__all__'


class BuildRegisterSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()
    CNPJ = serializers.StringRelatedField()
    class Meta:
        model = BuildRegisterModel
        fields = ("id", "owner", "name", "CNPJ")


class BuildInfoSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()
    CNPJ = serializers.StringRelatedField()

    class Meta:
        model = BuildInfoModel
        fields = ("id", 'name', 'CNPJ', 'address', 'email')