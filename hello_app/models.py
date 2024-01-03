from django.db import models

# Create your models here.
class std(models.Model):
    FullName=models.CharField(max_length=250)
    Email=models.CharField(max_length=250)
    Password=models.CharField(max_length=12)
    PhoneNumber=models.CharField(max_length=20)
    YearofCollege=models.CharField(max_length=20)
    department=models.CharField(max_length=20)

class dep(models.Model):
    Email=models.CharField(max_length=200)
    Password=models.CharField(max_length=12)



class proeditstd1(models.Model):
    img=models.ImageField(upload_to='images/')
    experience=models.TextField()
    skills=models.TextField()
    internships=models.TextField()
    workDone=models.TextField()
    workDetails=models.TextField()
    hobbies=models.TextField()
    achievements=models.TextField()

