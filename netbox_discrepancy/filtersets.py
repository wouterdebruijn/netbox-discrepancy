from netbox.filtersets import NetBoxModelFilterSet
from .models import Discrepancy, DiscrepancyType
from django.db.models import Q


class DiscrepancyTypeFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = DiscrepancyType
        fields = ['name']

    def search(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(description__icontains=value))


class DiscrepancyFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Discrepancy
        fields = ['device', 'type']

    def search(self, queryset, name, value):
        return queryset.filter(message__icontains=value)
