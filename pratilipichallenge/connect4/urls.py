from django.urls import path
from .views import ResultApiView

urlpatterns = [
    path('validity/', ResultApiView.as_view(), name='results')
]
