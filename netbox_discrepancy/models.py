from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from dcim.models import Device
from django.urls import reverse

class DiscrepancyType(NetBoxModel):
  name = models.CharField(max_length=50)
  description = models.TextField(blank=True, null=True)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('plugins:netbox_discrepancy:discrepancytype', args=[str(self.pk)])
  
  class Meta:
    verbose_name_plural = 'discrepancy types'

class Discrepancy(NetBoxModel):
  # Check if to=device works, or if it needs to be 'dcim.Device'
  device = models.ForeignKey(to=Device, on_delete=models.CASCADE)
  type = models.ForeignKey(to=DiscrepancyType, on_delete=models.CASCADE)
  
  message = models.TextField()

  def __str__(self):
    # Return message limited to 16
    return self.message[:16]
  
  def get_absolute_url(self):
    return reverse('plugins:netbox_discrepancy:discrepancy', args=[str(self.pk)])
  
  class Meta:
    verbose_name_plural = 'discrepancies'
 