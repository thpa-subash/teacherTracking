from django.db import models

class subjects(models.Model):
    subject = models.CharField(max_length=30,default="None")
    def __str__(self):
        return self.subject
class teacherDetails(models.Model):
    teachername = models.CharField(max_length=30 ,default="None")

    def __str__(self):
        return self.teachername

class semester(models.Model):
    semesters = models.CharField(max_length=30 ,default="None")

    def __str__(self):
        return self.semesters

class teacher(models.Model):
    teachername = models.ForeignKey(teacherDetails ,on_delete=models.CASCADE)
    teachesSemester=models.ForeignKey(semester ,on_delete=models.CASCADE)
    teachesSubjects = models.ForeignKey(subjects, on_delete=models.CASCADE)


    def __str__(self):
        return self.teachername.teachername
# Create your models here.
