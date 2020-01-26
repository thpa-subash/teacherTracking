from django.shortcuts import render
from .models import *

# Create your views here.
def home(request,id):
    teachers = teacher.objects.filter(teachername=id).order_by('teachesSemester')
    name = teacherDetails.objects.get(pk = id)
    print (name.teachername)
    return render(request,'details/home.html',{"teacher":teachers,'name':name})