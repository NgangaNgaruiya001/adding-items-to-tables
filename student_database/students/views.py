from django.shortcuts import render
from django.http import HttpResponse

from .models import *


# Create your views here.

def home(request):

	students = Student.objects.all()

	total_students = students.count()

	total_courses = Student.objects.values('programme').distinct().count()

	context = {'total_students' : total_students, 'total_courses': total_courses}


	return render(request, 'students/dashboard.html', context )

def student_data(request):

	students = Student.objects.all()

	return render(request, 'students/students.html', {'students' : students})
