from django.shortcuts import render
from django.views.generic import TemplateView

# Models import 
from core.models import BuildNameModel, BuildCNPJModel, BuildModel

# DRF / Serializers
from rest_framework import generics
from core.serializers import BuildNameSerializer, BuildCNPJSerializer, BuildModelSerializer

# Land Page
class IndexView(TemplateView):
    template_name: str = "index.html"


class BuildNameAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BuildNameSerializer
    queryset = BuildNameModel.objects.all()


class BuildCNPJAPI(generics.RetrieveAPIView):
    serializer_class = BuildCNPJSerializer
    queryset = BuildCNPJModel.objects.all()

    
class BuildAPI(generics.ListAPIView):
    serializer_class = BuildModelSerializer
    queryset = BuildModel.objects.all()