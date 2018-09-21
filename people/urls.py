from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from .views import EmployeeViewSet
app_name = 'people'

router = routers.DefaultRouter()

router.register(r'employee', EmployeeViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
]