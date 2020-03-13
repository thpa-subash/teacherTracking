from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def home(request):
    if request.is_ajax():

        teacher_id = request.POST['teacher']
        print (teacher_id)
        looks = Q(teachername__teachername__iexact=teacher_id)
        print (looks)
        if request.POST['r']:
            choosefeild = request.POST['r']
            print(choosefeild)
        look = Q(teachername__teachername__iexact=teacher_id, subject__subject=choosefeild)
        print (look)
        courseyear = teacher.objects.filter(look).values("courseComplete").order_by('year',
                                                                                    'teachesSemester').distinct()
        results = teacher.objects.filter(looks).order_by('year', 'teachesSemester')
        teachesyear = teacher.objects.filter(look).values("year").order_by('year').distinct()
        cours = []
        for cou in courseyear:
            for cour in cou.values():
                cours += cour,
        print (cours)
        year = []
        for yea in teachesyear:
            for ye in yea.values():
                year += ye,
        print(year)

    if request.method == 'POST':
        query = request.POST['q'].strip()





        if query :

            lookups = Q(teachername__teachername__iexact=query)
            choosefeild = teacher.objects.filter(lookups).values("subject__subject").last()
            for che in choosefeild.values():

                    sur=che
            print (sur)
            looku = Q(teachername__teachername__iexact=query,subject__subject=sur)
            lookup = Q(teachername__icontains=query)
            #
            results = teacher.objects.filter(lookups).order_by('year','teachesSemester')
            teachers = teacher.objects.filter(lookups).values("teachername").distinct()
            teacherer={}
            for te in teachers:
                for ears in te.values():
                    teacherer ['id']= ears

            print (teacherer)
            subj = teacher.objects.filter(lookups).values("subject__subject").distinct()
            course_year = teacher.objects.filter(looku).values("courseComplete").order_by('year','teachesSemester').distinct()
            print (course_year)
            teaches_year = teacher.objects.filter(lookups).values("year").order_by('year').distinct()
            cours=[]
            for cou in course_year:
                for cour in cou.values():
                    cours += cour,
            print (cours)
            year=[]
            for yea in teaches_year:
                for ye in yea.values():
                    year +=ye,
            print (year)
            result = teacherDetails.objects.filter(lookup).values('teachername')

            if results:
                teachernam = teacherDetails.objects.values("teachername")
                data = {}
                for ik in teachernam:
                    for val in ik.values():
                        data[val] = ""
                print(data)
                return render(request,'details/index.html',{'se':results,'data':data,'subje':subj,'teacher':query,'teachers_year':year,'course':cours})
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

    return render(request,'details/index.html',{"data":data,})

def home1(request):
    if request.is_ajax():
        choosefeild = request.POST['r']
        print(choosefeild)

        teacher_id = request.POST['teacher']
        print (teacher_id)
        looks = Q(teachername__teachername__iexact=teacher_id)
        print (looks)
    #     if request.POST['r']:
    #         choosefeild = request.POST['r']
    #         print(choosefeild)
        mlook = Q(teachername__teachername__iexact=teacher_id, subject__subject=choosefeild)
        print (mlook)
        mcourseyear = teacher.objects.filter(mlook).values("courseComplete").order_by('year',
                                                                                     'teachesSemester').distinct()
    #     results = teacher.objects.filter(looks).order_by('year', 'teachesSemester')
        teachesyear = teacher.objects.filter(mlook).values("year").order_by('year').distinct()
        mcours = []
        for cou in mcourseyear:
            for cour in cou.values():
                mcours += cour,
        print (mcours)
        year = []
        for yea in teachesyear:
            for ye in yea.values():
               year += ye,
        print(year)

        return render(request,'details/search.html',{'teachers_year':year,'course':mcours})

    if request.method == 'POST':
        query = request.POST['q'].strip()
        lookups = Q(teachername__teachername__iexact=query)

        if teacher.objects.filter(teachername__teachername__iexact=query):




            choosefeild = teacher.objects.filter(lookups).values("subject__subject").last()
            print (choosefeild)
            print("i am here")
            if choosefeild:
                for che in choosefeild.values():
                    sur = che
                    #display lastsubjects in list
            looku = Q(teachername__teachername__iexact=query, subject__subject=che)
            course_year = teacher.objects.filter(looku).values("courseComplete").order_by('year',
                                                                                                  'teachesSemester').distinct()
            cours = []
            for cou in course_year:
                for cour in cou.values():
                    cours += cour,
                print (cours)
                #search the subjects and teachername

            lookup = Q(teachername__icontains=query)

            #
            results = teacher.objects.filter(lookups).order_by('year', 'teachesSemester')
            teachers = teacher.objects.filter(lookups).values("teachername").distinct()
            teacherer = {}
            for te in teachers:
                for ears in te.values():
                    teacherer['id'] = ears
            #teachers ID retrive
            subj = teacher.objects.filter(lookups).values("subject__subject").distinct()

            #retrive total course data in queryset
            teaches_year = teacher.objects.filter(lookups).values("year").order_by('year').distinct()
            cours = []
            for cou in course_year:
                for cour in cou.values():
                    cours += cour,
            print (cours)
            year = []
            for yea in teaches_year:
                for ye in yea.values():
                    year += ye,
            print (year)
            result = teacherDetails.objects.filter(lookup).values('teachername')

            if results:
                teachernam = teacherDetails.objects.values("teachername")
                data = {}
                for ik in teachernam:
                    for val in ik.values():
                        data[val] = ""
                print(data)
                return render(request, 'details/index.html',
                              {'se': results, 'data': data,'subje':subj,  'teacher': query,'teachers_year':year,'course':cours,
                               })
            else:
                return render(request, 'details/index.html', {'result': result})
                messages.error(request, 'Result  not found')
        else:
            messages.error(request, 'Result  not found')
            lookup = Q(teachername__icontains=query)
            result = teacherDetails.objects.filter(lookup).values('teachername')
            return render(request, 'details/index.html', {'result': result})
            print("ashish is here")

    # teachers = teacher.objects.filter(teachername=id).order_by('year','teachesSemester')
    # name = teacherDetails.objects.get(pk = id)
    # print (name.teachername)
    # return render(request,'details/index.html',{"teacher":teachers,'name':name})
    teachernam = teacherDetails.objects.values("teachername")
    data = {}
    for ik in teachernam:
            for val in ik.values():
                data[val] = ""

    return render(request, 'details/index.html', {"data": data })