from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'enrollment_date', 'grade']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter date of birth'}),
            'enrollment_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter enrollment date'}),
            'grade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter grade'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'date_of_birth': 'Date of Birth',
            'enrollment_date': 'Enrollment Date',
            'grade': 'Grade',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("This field is required.")
        if not "@" in email:
            raise forms.ValidationError("Enter a valid email address.")
        return email

    def clean_grade(self):
        grade = self.cleaned_data.get('grade')
        if grade < 1 or grade > 12:
            raise forms.ValidationError("Grade must be between 1 and 12.")
        return grade