from django.urls import path
from .views import GamePlayApiView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('validity/', GamePlayApiView, 'results')
urlpatterns = router.urls