from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_discrepancy'

router = NetBoxRouter()
router.register('discrepancytypes', views.DiscrepancyTypeViewSet)
router.register('discrepancies', views.DiscrepancyViewSet)

urlpatterns = router.urls