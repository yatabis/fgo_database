from rest_framework import routers

from .views import ServantViewSet, ClassViewSet

router = routers.DefaultRouter()
router.register('servants', ServantViewSet)
router.register('classes', ClassViewSet)
