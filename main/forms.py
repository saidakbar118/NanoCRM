from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

    
class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'parol'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError("Bunday foydalanuvchi topilmadi!")

        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Noto‘g‘ri parol!")

        self.user = user
        return cleaned_data

    def get_user(self):
        return self.user

    
class BaseProfileUserForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Foydalanuvchi nomi'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'})
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = ProfileUser
        fields = [
            'username', 'password', 'full_name', 'address', 'phone_number', 'department',
            'description', 'birth_date', 'role', 'group', 'profile_pic'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ism, familiya"}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manzil'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqam'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mutaxassislik'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Qo'shimcha ma'lumot", 'rows': 3}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Bunday foydalanuvchi nomi allaqachon mavjud.")
        return username

    def save(self, commit=True):
        username = self.cleaned_data.pop('username')
        password = self.cleaned_data.pop('password')

        # Avval User obyektini yaratamiz va saqlaymiz
        user = User(username=username)
        user.set_password(password)
        user.save()  # ← MUHIM QADAM

        # Endi ProfileUser ni yaratamiz
        profile = super().save(commit=False)
        profile.user = user  # bog'lab qo'yamiz

        if commit:
            profile.save()

        return profile
    
class ProfessorForm(BaseProfileUserForm):
    class Meta(BaseProfileUserForm.Meta):
        fields = [
            'username', 'password', 'full_name', 'address', 'phone_number',
            'department', 'description', 'birth_date', 'profile_pic'
        ]
        
class StudentForm(BaseProfileUserForm):
    class Meta(BaseProfileUserForm.Meta):
        fields = [
            'username', 'password', 'full_name', 'address', 'phone_number',
            'description', 'birth_date', 'group', 'profile_pic'
        ]


    
class CoursesForm(forms.ModelForm):
    class Meta:
        model = add_course_model
        fields = ['name','time','course_price','department','description','professor','days']
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Guruh nomi"}),
            'time':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Guruh vaqti"}),
            'days':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Guruh kunlari"}),
            'course_price':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Tarif narxi"}),
            'department':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Yo'nalish"}),
            'description':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Qo'shimcha ma'lumot"}),
            'professor': forms.Select(attrs={'class': 'form-control'}),
        }
        
        
class StudentEditForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ['full_name', 'address', 'phone_number', 'birth_date', 'description', 'profile_pic']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        
        
        
