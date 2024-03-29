from utilities.testing import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model
from django.test import Client
from ..models import Discrepancy, DiscrepancyType
from dcim.models import Device, DeviceType, Manufacturer, Site, DeviceRole


User = get_user_model()


class DiscrepancyViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser')
        self.add_permissions('netbox_discrepancy.view_discrepancy')
        self.add_permissions('netbox_discrepancy.view_discrepancytype')
        self.add_permissions('netbox_discrepancy.add_discrepancy')
        self.add_permissions('netbox_discrepancy.add_discrepancytype')
        self.add_permissions('netbox_discrepancy.change_discrepancy')
        self.add_permissions('netbox_discrepancy.change_discrepancytype')
        self.add_permissions('netbox_discrepancy.delete_discrepancy')
        self.add_permissions('netbox_discrepancy.delete_discrepancytype')

        self.client = Client()
        self.client.force_login(self.user)

        self.site = Site.objects.create(name='Test Site')
        self.manufacturer = Manufacturer.objects.create(
            name='Test Manufacturer')
        self.device_type = DeviceType.objects.create(
            manufacturer=self.manufacturer, model='Test Device Type',
            slug='test-device-type',
        )
        self.device_role = DeviceRole.objects.create(
            name='Test Device Role')

        self.device = Device.objects.create(
            device_type=self.device_type,
            name='Test Device',
            site=self.site,
            role=self.device_role,
        )

        self.discrepancy_type = DiscrepancyType.objects.create(
            name='Test Discrepancy Type')
        self.discrepancy = Discrepancy.objects.create(
            type=self.discrepancy_type,
            device=self.device,
            message='Test Field Discrepancy Message',
        )

    def test_discrepancy_list_view(self):
        url = reverse('plugins:netbox_discrepancy:discrepancy_list')

        response = self.client.get(url)
        self.assertHttpStatus(response, 200)

    def test_discrepancy_type_list_view(self):
        url = reverse('plugins:netbox_discrepancy:discrepancytype_list')
        response = self.client.get(url)
        self.assertHttpStatus(response, 200)

    def test_discrepancy_type_add_view(self):
        url = reverse('plugins:netbox_discrepancy:discrepancytype_add')
        response = self.client.get(url)
        self.assertHttpStatus(response, 200)

    def test_discrepancy_type_edit_view(self):
        url = reverse(
            'plugins:netbox_discrepancy:discrepancytype_edit', args=[self.discrepancy_type.pk])
        response = self.client.get(url)
        self.assertHttpStatus(response, 200)

    def test_discrepancy_type_delete_view(self):
        url = reverse(
            'plugins:netbox_discrepancy:discrepancytype_delete', args=[self.discrepancy_type.pk])
        response = self.client.get(url)
        self.assertHttpStatus(response, 200)

    def test_discrepancy_add_view(self):
        url = reverse('plugins:netbox_discrepancy:discrepancy_add')
        response = self.client.get(url)
        self.assertHttpStatus(response, 200)

    def test_discrepancy_edit_view(self):
        url = reverse('plugins:netbox_discrepancy:discrepancy_edit',
                      args=[self.discrepancy.pk])
        response = self.client.get(url)
        self.assertHttpStatus(response, 200)

    def test_discrepancy_delete_view(self):
        url = reverse(
            'plugins:netbox_discrepancy:discrepancy_delete', args=[self.discrepancy.pk])
        response = self.client.get(url)
        self.assertHttpStatus(response, 200)
