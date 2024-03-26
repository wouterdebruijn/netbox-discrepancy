from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from .models import Discrepancy, DiscrepancyType
from dcim.models import Device


class DiscrepancyTypeForm(NetBoxModelForm):
    class Meta:
        model = DiscrepancyType
        fields = ('name', 'description')


class DiscrepancyForm(NetBoxModelForm):
    class Meta:
        model = Discrepancy
        fields = ('device', 'type', 'message')


class DiscrepancyFilterForm(NetBoxModelFilterSetForm):
    model = Discrepancy

    device = forms.ModelChoiceField(
        queryset=Device.objects.all(), required=False)
    type = forms.ModelChoiceField(
        queryset=DiscrepancyType.objects.all(),
        required=False)
