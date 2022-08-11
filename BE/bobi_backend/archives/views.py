from rest_framework.response import Response
from .models import ArchiveImage, ArchiveVideo
from rest_framework import viewsets
from .serializers import ArchiveImageSerializer, ArchiveImageSerializer, ArchiveVideoSerializer

# Create your views here.
class ArchiveImageViewSet(viewsets.ModelViewSet):
    queryset = ArchiveImage.objects.all()
    serializer_class = ArchiveImageSerializer


class ArchiveVideoViewSet(viewsets.ModelViewSet):
    queryset = ArchiveVideo.objects.all()
    serializer_class = ArchiveVideoSerializer