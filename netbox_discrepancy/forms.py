from netbox.forms import NetBoxModelForm
from .models import Discrepancy, DiscrepancyType

class DiscrepancyTypeForm(NetBoxModelForm):
  class Meta:
    model = DiscrepancyType
    fields = ['name', 'description', 'tags']

class DiscrepancyForm(NetBoxModelForm):
  class Meta:
    model = Discrepancy
    fields = ['device', 'type', 'message', 'tags']