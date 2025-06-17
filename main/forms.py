from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol yarating'}),
        label='Parol'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parolni qayta kiriting'}),
        label='Parol'
    )
    ROLE_CHOICES = [
        ('teacher', "O'qituvchi"),
        ('student', "Talaba"),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect, label='Rolni tanlang')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role']
        widgets = {
            'username': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        }
        labels = {
            'username': 'Email'
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Bunday foydalanuvchi allaqachon mavjud!')
        return username

    def clean_password2(self):
        p1 = self.cleaned_data.get('password1')
        p2 = self.cleaned_data.get('password2')
        if p1 and p2 and p1 != p2:
            raise ValidationError('Parollar mos emas')
        return p2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    
class LoginForm(forms.Form):
    user_or_phone = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'})
    )

    def clean(self):
        cleaned_data = super().clean()
        user_or_phone = cleaned_data.get('user_or_phone')
        password = cleaned_data.get('password')

        # Faqat username orqali topamiz
        user = User.objects.filter(username=user_or_phone).first()
        if not user:
            raise forms.ValidationError("Bunday foydalanuvchi topilmadi!")

        # ✅ Parolni tekshiramiz
        user = authenticate(username=user.username, password=password)
        if not user:
            raise forms.ValidationError("Noto‘g‘ri parol!")

        self.user = user
        return cleaned_data

    def get_user(self):
        return self.user

    
    
class RegisterProfessorForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = add_professor_model
        fields = ['full_name', 'address', 'phone_number', 'birth_date', 'department', 'description', 'gender']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ism Familiya'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manzil'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+998-00-000-00-00'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kafedra yoki bo‘lim'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }
        
class RegisterStudentForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = add_student_model
        fields = ['full_name', 'address', 'phone_number', 'birth_date', 'description', 'gender', 'group']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ism Familiya'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manzil'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+998-00-000-00-00'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }

class ProfessorForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    class Meta:
        model = add_professor_model
        fields = ['full_name','address','phone_number','birth_date','department','description','gender']
        widgets = {
            'full_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ism,familiya"}),
            'address':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'phone_number':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqam'}),
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
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    class Meta:
        model = add_student_model
        fields = ['full_name','address','phone_number','birth_date','description','gender','group']
        widgets = {
            'full_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ism,familiya"}),
            'address':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'phone_number':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqam'}),
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
        
        
        
