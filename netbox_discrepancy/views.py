from django.shortcuts import redirect
from netbox.views import generic
from . import forms, models, tables, filtersets
from dcim.models import Device
from utilities.views import ViewTab, register_model_view

# DiscrepancyType


class DiscrepancyTypeView(generic.ObjectView):
    queryset = models.DiscrepancyType.objects.all()


class DiscrepancyTypeListView(generic.ObjectListView):
    queryset = models.DiscrepancyType.objects.all()
    table = tables.DiscrepancyTypeTable


class DiscrepancyTypeEditView(generic.ObjectEditView):
    queryset = models.DiscrepancyType.objects.all()
    form = forms.DiscrepancyTypeForm


class DiscrepancyTypeDeleteView(generic.ObjectDeleteView):
    queryset = models.DiscrepancyType.objects.all()

# Discrepancy


class DiscrepancyView(generic.ObjectView):
    queryset = models.Discrepancy.objects.all()


class DiscrepancyListView(generic.ObjectListView):
    queryset = models.Discrepancy.objects.all()
    table = tables.DiscrepancyTable
    filterset = filtersets.DiscrepancyFilterSet
    filterset_form = forms.DiscrepancyFilterForm


class DiscrepancyEditView(generic.ObjectEditView):
    queryset = models.Discrepancy.objects.all()
    form = forms.DiscrepancyForm


class DiscrepancyDeleteView(generic.ObjectDeleteView):
    queryset = models.Discrepancy.objects.all()


@register_model_view(Device, name="discrepancy", )
class DeviceDiscrepancyView(generic.ObjectChildrenView):
    child_model = models.Discrepancy
    table = tables.DiscrepancyTable
    template_name = 'generic/object_children.html'
    tab = ViewTab(
        label='Discrepancies',
        badge=lambda obj: models.Discrepancy.objects.filter(
            device=obj).count(),
    )

    queryset = Device.objects.all()
    filterset = filtersets.DiscrepancyFilterSet
    filterset_form = forms.DiscrepancyFilterForm

    def get_children(self, request, parent):
        return models.Discrepancy.objects.filter(device=parent.pk)
