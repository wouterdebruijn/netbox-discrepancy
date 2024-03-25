from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import DiscrepancyType, Discrepancy

class DiscrepancyTypeSerializer(NetBoxModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_discrepancy-api:discrepancytype-detail')

  class Meta:
    model = DiscrepancyType
    fields = ('id', 'name', 'description', 'created', 'last_updated', 'url')


class NestedDiscrepancyTypeSerializer(WritableNestedSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_discrepancy-api:discrepancytype-detail')

  class Meta:
    model = DiscrepancyType
    fields = ('id', 'name', 'description', 'url')

class DiscrepancySerializer(NetBoxModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_discrepancy-api:discrepancy-detail')
  type = NestedDiscrepancyTypeSerializer()

  class Meta:
    model = Discrepancy
    fields = ('id', 'device', 'type', 'message', 'created', 'last_updated', 'url')

class NestedDiscrepancySerializer(WritableNestedSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_discrepancy-api:discrepancy-detail')
  type = NestedDiscrepancyTypeSerializer()

  class Meta:
    model = Discrepancy
    fields = ('id', 'device', 'type', 'message', 'url')

