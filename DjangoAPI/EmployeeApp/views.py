from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.


@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(
            DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(
            department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Upadated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == "GET":
        employee = Employees.objects.all()
        employee_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data, safe=False)

    if request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Data added successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)

    if request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(
            EmployeeId=employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    if request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)
