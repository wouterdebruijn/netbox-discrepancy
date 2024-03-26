from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = [
    path(
        'overview',
        views.DiscrepancyOverview.as_view(),
        name='overview'),
    path(
        'discrepancy/',
        views.DiscrepancyListView.as_view(),
        name='discrepancy_list'),
    path(
        'discrepancy/add/',
        views.DiscrepancyEditView.as_view(),
        name='discrepancy_add'),
    path(
        'discrepancy/<int:pk>/',
        views.DiscrepancyView.as_view(),
        name='discrepancy'),
    path(
        'discrepancy/<int:pk>/edit/',
        views.DiscrepancyEditView.as_view(),
        name='discrepancy_edit'),
    path(
        'discrepancy/<int:pk>/delete/',
        views.DiscrepancyDeleteView.as_view(),
        name='discrepancy_delete'),
    path(
        'discrepancytype/',
        views.DiscrepancyTypeListView.as_view(),
        name='discrepancytype_list'),
    path(
        'discrepancytype/add/',
        views.DiscrepancyTypeEditView.as_view(),
        name='discrepancytype_add'),
    path(
        'discrepancytype/<int:pk>/',
        views.DiscrepancyTypeView.as_view(),
        name='discrepancytype'),
    path(
        'discrepancytype/<int:pk>/edit/',
        views.DiscrepancyTypeEditView.as_view(),
        name='discrepancytype_edit'),
    path(
        'discrepancytype/<int:pk>/delete/',
        views.DiscrepancyTypeDeleteView.as_view(),
        name='discrepancytype_delete'),
    path(
        'discrepancy/<int:pk>/changelog/',
        ObjectChangeLogView.as_view(),
        name='discrepancy_changelog',
        kwargs={
            'model': models.Discrepancy}),
    path(
        'discrepancytype/<int:pk>/changelog/',
        ObjectChangeLogView.as_view(),
        name='discrepancytype_changelog',
        kwargs={
            'model': models.DiscrepancyType}),
]
