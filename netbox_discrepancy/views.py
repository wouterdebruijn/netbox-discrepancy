from netbox.views import generic
from . import forms, models, tables, filtersets
from dcim.models import Device
from utilities.views import ViewTab, register_model_view
from django.views.generic import View
from django.shortcuts import render
from django_tables2.columns import LinkColumn

from core.models import Job
from core.tables import JobTable

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


class DiscrepancyOverview(View):
    def get(self, request):

        class CustomTable(JobTable):
            job_id = LinkColumn()

            class Meta(JobTable.Meta):
                default_columns = ('status', 'created',
                                   'completed', 'scheduled', 'job_id')

        jobs = Job.objects.filter(name="Synchronize discrepancies").all()
        job_table = CustomTable(jobs)

        job_table

        return render(request, 'netbox_discrepancy/overview.html', {
            'job_table': job_table,
        })
