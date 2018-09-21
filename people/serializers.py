from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from .models import Employee, ContactDetails


class ContactSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ContactDetails
        fields = "__all__"


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','name','dob','designation','experience','joining_date','referred_by','contact','photo_url','status')


