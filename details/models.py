from django.db import models

class subjects(models.Model):
    subject = models.CharField(max_length=30,default="None")
    def __str__(self):
        return self.subject
class teacherDetails(models.Model):
    teachername = models.CharField(max_length=30 ,default="None")

    def __str__(self):
        return self.teachername

class program(models.Model):
    programs = models.CharField(max_length=30,default="None" )

    def __str__(self):
        return self.programs

class semester(models.Model):
    semesters = models.CharField(max_length=30 ,default="None")

    def __str__(self):
        return self.semesters


year =[("2000",2000),
       ('2001',2001),
       ('2002',2002),]
class teacher(models.Model):
    teachername = models.ForeignKey(teacherDetails ,on_delete=models.CASCADE)
    year = models.CharField(
        max_length=7,
        choices=year,
        default="Select a Year",)
    program = models.ForeignKey(program ,on_delete=models.CASCADE)
    teachesSemester=models.ForeignKey(semester ,on_delete=models.CASCADE)
    teachesSubjects = models.ForeignKey(subjects, on_delete=models.CASCADE)
    courseComplete = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.teachername.teachername
# Create your models here.
