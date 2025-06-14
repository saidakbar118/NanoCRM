from django import forms
from .models import *
from django.core.exceptions import ValidationError

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = add_professor_model
        fields = ['full_name','address','phone_number','birth_date','postcode','department','description','gender']
        widgets = {
            'full_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ism,familiya"}),
            'address':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'phone_number':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqam'}),
            'birth_date':forms.DateInput(attrs={'class': 'form-control', 'placeholder': "YYYY.MM.DD"}),
            'postcode':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unikal raqam'}),
            'phone_number':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqam kiriting'}),
            'department':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Mutahasislik"}),
            'description':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Qo'shimcha"}),
        }
        
        
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit() or len(phone) != 13:
            raise ValidationError("Telefon raqam 13tadan iborat bo'lishi kerak!")
        return phone
    
    
class StudentForm(forms.ModelForm):
    class Meta:
        model = add_student_model
        fields = ['full_name','address','phone_number','birth_date','postcode','description','gender','group']
        widgets = {
            'full_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ism,familiya"}),
            'address':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'phone_number':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqam'}),
            'birth_date':forms.DateInput(attrs={'class': 'form-control', 'placeholder': "YYYY.MM.DD"}),
            'postcode':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unikal raqam'}),
            'phone_number':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqam kiriting'}),
            'description':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Qo'shimcha"}),
        }
        
        
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit() or len(phone) != 13:
            raise ValidationError("Telefon raqam 13tadan iborat bo'lishi kerak!")
        return phone
    
class CoursesForm(forms.ModelForm):
    class Meta:
        model = add_course_model
        fields = ['name','time','course_price','department','description','professor']
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Guruh nomi"}),
            'time':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Guruh vaqti"}),
            'course_price':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Tarif narxi"}),
            'department':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Yo'nalish"}),
            'description':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Qo'shimcha ma'lumot"}),
        }
        
        
        
