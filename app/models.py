from django.db import models

# Create your models here.
class Course(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=10)
    c_details=models.URLField()
    def __str__(self):
        return self.cname

class Student(models.Model):
    std_id=models.IntegerField()
    std_name=models.CharField(max_length=5)
    std_courst=models.CharField(max_length=10)
    c_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return self.std_name


class AccessRecord(models.Model):
    std_name=models.ForeignKey(Student,on_delete=models.CASCADE) # std_name takes reference of Student std_name  so here it takes pk values
    assigned_staff=models.CharField(max_length=10)
    access_date=models.DateField()
    def __str__(self) -> str:
        return str(self.pk)
    










