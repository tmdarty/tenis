from django.db import models

# Create your models here.

class Staff(models.Model):
    staff_name = models.CharField(max_length=25)
    contact = models.CharField(max_length=25)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(choices=GENDER_CHOICES, default='Select gender', max_length=20)
    date_employed = models.DateField(auto_now=True)

class Department(models.Model):
    dept_name = models.CharField(max_length=25)

class Courses(models.Model):
    course_name = models.CharField(max_length=25)
    course_code = models.CharField(max_length=25)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)

class CourseUnit(models.Model):
    unit_name = models.CharField(max_length=25)
    unit_code = models.CharField(max_length=25)
    course_name = models.ForeignKey(Courses, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

class Students(models.Model):
    name = models.CharField(max_length=25)
    student_reg_no = models.CharField(max_length=25, unique=True)
    student_email = models.EmailField(max_length=25)
    student_phone = models.CharField(max_length=25)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    reg_date = models.DateField()

