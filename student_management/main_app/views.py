from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'main_app/student_list.html'
    context_object_name = 'students'
    paginate_by = 10  # Number of students per page

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Student.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query)).order_by('first_name')
        return Student.objects.all().order_by('first_name')
    
    def get_paginate_by(self, queryset):
        paginate_by = self.request.GET.get('paginate_by', 10)
        try:
            paginate_by = int(paginate_by)
            if paginate_by < 1:
                paginate_by = 10
        except ValueError:
            paginate_by = 10
        return paginate_by
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_obj = context['page_obj']
        context['start_index'] = page_obj.start_index()
        context['end_index'] = page_obj.end_index()
        return context

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')
