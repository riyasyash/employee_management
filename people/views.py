from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Employee
from .serializers import EmployeeSerializer, ContactSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('name')
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        conatct_data = request.data.get('contact')
        contact_serializer = ContactSerializer(data=conatct_data)
        contact_serializer.is_valid()
        contact = contact_serializer.save()
        employee_data = request.data
        employee_data.update({'contact':contact.id})
        employee_serializer = EmployeeSerializer(data=employee_data)
        employee_serializer.is_valid()
        employee = employee_serializer.save()
        # employee.contact = contact
        # employee.save()
        return Response(EmployeeSerializer(employee).data)

    def list(self, request, *args, **kwargs):
        # alumni = Employee.objects.filter(status=False).all()
        # alumies = EmployeeSerializer(alumni, many=True).data
        # employee = Employee.objects.filter(status=True).all()
        # employees = EmployeeSerializer(employee, many=True).data
        #
        # return Response({
        #     'alumni':alumies,
        #     'employee':employees
        # })
        if request.GET.get('search_key'):
            search_key = request.GET.get('search_key')
            employee = Employee.objects.filter(Q(name__icontains=search_key)|Q(designation__icontains=search_key)).all()
        else:
            employee = Employee.objects.all()
        return Response(EmployeeSerializer(employee,many=True).data)

    def retrieve(self, request, *args, **kwargs):
        employee = Employee.objects.get(id=kwargs.get('pk'))
        return Response({
            'id':employee.id,
            'name':employee.name,
            'designation':employee.designation,
            'joining_date':employee.joining_date,
            'referred_by':employee.referred_by.name if employee.referred_by else None,
            'experience':employee.experience,
            'photo_url':employee.photo_url,
            'status':employee.status,
            'dob':employee.dob,
            'sex':employee.sex,
            'contact':{
                'address':employee.contact.address if employee.contact else None,
                'mobile':employee.contact.mobile  if employee.contact else None,
                'email':employee.contact.email  if employee.contact else None
            }
        })