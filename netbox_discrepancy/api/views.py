from netbox.api.viewsets import NetBoxModelViewSet

from .. import models
from .serializers import DiscrepancySerializer, DiscrepancyTypeSerializer


class DiscrepancyTypeViewSet(NetBoxModelViewSet):
    queryset = models.DiscrepancyType.objects.all()
    serializer_class = DiscrepancyTypeSerializer


class DiscrepancyViewSet(NetBoxModelViewSet):
    queryset = models.Discrepancy.objects.all()
    serializer_class = DiscrepancySerializer
