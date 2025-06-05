from django.shortcuts import render
from django.http import HttpResponse

def student(request):
    students = [
        {'name':'sahil', 'age':22}
    ]
    return HttpResponse(students)