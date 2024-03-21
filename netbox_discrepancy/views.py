from netbox.views import generic
from . import forms, models, tables

# DiscrepancyType
class DiscrepancyTypeView(generic.ObjectView):
  queryset = models.DiscrepancyType.objects.all()

class DiscrepancyTypeListView(generic.ObjectListView):
  queryset = models.DiscrepancyType.objects.all()
  table = tables.DiscrepancyTypeTable

class DiscrepancyTypeEditView(generic.ObjectEditView):
  queryset = models.DiscrepancyType.objects.all()
  model_form = forms.DiscrepancyTypeForm

class DiscrepancyTypeDeleteView(generic.ObjectDeleteView):
  queryset = models.DiscrepancyType.objects.all()

# Discrepancy
class DiscrepancyView(generic.ObjectView):
  queryset = models.Discrepancy.objects.all()

class DiscrepancyListView(generic.ObjectListView):
  queryset = models.Discrepancy.objects.all()
  table = tables.DiscrepancyTable

class DiscrepancyEditView(generic.ObjectEditView):
  queryset = models.Discrepancy.objects.all()
  model_form = forms.DiscrepancyForm

class DiscrepancyDeleteView(generic.ObjectDeleteView):
  queryset = models.Discrepancy.objects.all()

