from django.db import models

class add_professor_model(models.Model):
    
    GENDER_CHOICES = [
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
        ('Boshqa', 'Boshqa')
    ]
    
    full_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=90)
    birth_date = models.CharField(max_length=90)
    postcode = models.IntegerField()
    department = models.CharField(max_length=150)
    description = models.TextField()  
    gender = models.CharField(max_length=90, choices=GENDER_CHOICES)     
    
    def __str__(self):
        return self.full_name 

class add_course_model(models.Model):
    name = models.CharField(max_length=150)
    time = models.CharField(max_length=90)
    course_price = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    description = models.TextField()
    professor = models.ForeignKey(add_professor_model,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class add_student_model(models.Model):
    
    GENDER_CHOICES = [
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
        ('Boshqa', 'Boshqa')
    ]
    
    full_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=90)
    birth_date = models.CharField(max_length=90)
    postcode = models.IntegerField()
    description = models.TextField()  
    gender = models.CharField(max_length=90, choices=GENDER_CHOICES) 
    group = models.ForeignKey(add_course_model,on_delete=models.CASCADE)    
    
    def __str__(self):
        return self.full_name 
    
