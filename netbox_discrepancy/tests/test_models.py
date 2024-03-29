from django.test import TestCase
from ..models import Discrepancy, DiscrepancyType
from dcim.models import Device, DeviceType, Manufacturer, Site, DeviceRole


class DiscrepancyModelTestCase(TestCase):
    def setUp(self):
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

    def test_discrepancy_str(self):
        self.assertEqual(str(self.discrepancy),
                         'Test Field Discr')

    def test_discrepancy_type_str(self):
        self.assertEqual(str(self.discrepancy_type), 'Test Discrepancy Type')

    def test_discrepancy_type_get_absolute_url(self):
        self.assertEqual(
            self.discrepancy_type.get_absolute_url(), f'/plugins/discrepancy/discrepancytype/{self.discrepancy_type.pk}/')

    def test_discrepancy_get_absolute_url(self):
        self.assertEqual(self.discrepancy.get_absolute_url(),
                         f'/plugins/discrepancy/discrepancy/{self.discrepancy.pk}/')
