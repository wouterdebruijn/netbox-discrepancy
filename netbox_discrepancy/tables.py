import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import Discrepancy, DiscrepancyType

class DiscrepancyTypeTable(NetBoxTable):
  class Meta(NetBoxTable.Meta):
    model = DiscrepancyType
    fields = ('name', 'description', 'tags')
    columns = ('name', 'description', 'tags')

class DiscrepancyTable(NetBoxTable):
  class Meta(NetBoxTable.Meta):
    model = Discrepancy
    fields = ('device', 'type', 'message', 'tags')
    columns = ('device', 'type', 'message', 'tags')