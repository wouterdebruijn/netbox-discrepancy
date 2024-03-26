from netbox.filtersets import NetBoxModelFilterSet
from .models import Discrepancy
from django.db.models import Q


class DiscrepancyFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Discrepancy
        fields = ['device', 'type']

    def search(self, queryset, name, value):
        return queryset.filter(message__icontains=value)
