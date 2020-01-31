from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == 'POST':
        query = request.POST['q'].strip()
        print (query)


        if query :

            lookups = Q(teachername__teachername__iexact=query)
            lookup = Q(teachername__icontains=query)

            results = teacher.objects.filter(lookups).order_by('year','teachesSemester')
            result = teacherDetails.objects.filter(lookup).values('teachername')

            if results:
                teachernam = teacherDetails.objects.values("teachername")
                data = {}
                for ik in teachernam:
                    for val in ik.values():
                        data[val] = ""
                return render(request,'details/index.html',{'se':results,'data':data})
            else:
                return render(request,'details/index.html',{'result':result})
                messages.error(request,'Result  not found')
        else:
            messages.error(request,'Result  not found')
    # teachers = teacher.objects.filter(teachername=id).order_by('year','teachesSemester')
    # name = teacherDetails.objects.get(pk = id)
    # print (name.teachername)
    #return render(request,'details/index.html',{"teacher":teachers,'name':name})
    teachernam = teacherDetails.objects.values("teachername")
    data={}
    for ik in teachernam:
        for val in ik.values():


            data[val]=""
    print (data)
    return render(request,'details/index.html',{"data":data,})

def search(request):
    if request.method == 'POST':
        query = request.POST['q']


        if query :

            lookups = Q(teachername__icontains=query)

            results = std_detail.objects.filter(lookups).order_by('teachername')
            print(results)
            if results:
                return render(request,'students/search.html',{'se':results})
            else:
                messages.error(request,'Result  not found')
        else:
            return HttpResponseRedirect("/students/search/")

    return render(request, 'details/index.html')