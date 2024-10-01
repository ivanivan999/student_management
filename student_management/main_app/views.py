from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

def student_list(request):
	students = Student.objects.all()
	return render(request, 'student_list.html', {'students': students})

def student_detail(request, pk):
	student = get_object_or_404(Student, pk=pk)
	return render(request, 'student_detail.html', {'student': student})

def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})