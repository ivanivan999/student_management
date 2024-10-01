from django.shortcuts import render, get_object_or_404, redirect
from .models import Student

def student_list(request):
	students = Student.objects.all()
	return render(request, 'student_list.html', {'students': students})

def student_detail(request, pk):
	student = get_object_or_404(Student, pk=pk)
	return render(request, 'student_detail.html', {'student': student})

