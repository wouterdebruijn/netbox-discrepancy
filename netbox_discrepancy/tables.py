import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import Discrepancy, DiscrepancyType


class DiscrepancyTypeTable(NetBoxTable):
    name = tables.LinkColumn()

    class Meta(NetBoxTable.Meta):
        model = DiscrepancyType
        fields = ('name', 'description')
        columns = ('name', 'description')


class DiscrepancyTable(NetBoxTable):
    device = tables.LinkColumn()
    type = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = Discrepancy
        fields = ('id', 'device', 'type', 'message')
        columns = ('id', 'device', 'type', 'message')
