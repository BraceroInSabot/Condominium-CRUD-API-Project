from django.shortcuts import render
from django.views.generic import TemplateView

# Models import 
from core.models import BuildNameModel, BuildModel

# DRF / Serializers
from rest_framework import generics
from core.serializers import BuildNameSerializer, BuildModelSerializer

# Land Page
class IndexView(TemplateView):
    template_name: str = "index.html"


class BuildNameAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BuildNameSerializer
    queryset = BuildNameModel.objects.all()


class BuildAPI(generics.ListAPIView):
    serializer_class = BuildModelSerializer
    queryset = BuildModel.objects.all()