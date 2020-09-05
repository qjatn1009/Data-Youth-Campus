from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Students

#CUD는 HttpResposeRedirect해야됨
# Create your views here.
def student_regform(request):
    return render(request, 'students/register_student.html')

def student_register(request):
    name = request.POST['name'] #값을 받아오는 것
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']
    qs = Students(s_name = name, s_major = major, s_age = age, s_grade = grade, s_gender = gender)
    qs.save()
    # return render(request, 'students/register_student.html')
    return HttpResponseRedirect(reverse('search'))

def student_insert(request):
    qs = Students(s_name = 'son', s_major='',
                    s_age =' ', s_grade = '',
                    s_gender='')
    return qs

def student_search(request):
    qs = Students.objects.all()
    context = {'student_list': qs}
    return render(request, 'students/search_student.html', context)

def student_detail(request, name):
    qs = Students.objects.get(s_name = name)
    print(qs)
    context = {'student_info': qs}
    return render(request, 'students/detail_student.html', context)

def student_modiform(request, name):
    qs = Students.objects.get(s_name = name)
    context = {'student_info': qs}
    return render(request, 'students/modify_student.html', context)

def student_modify(request):
    name = request.POST['name'] #값을 받아오는 것
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']
    
    s_qs = Students.objects.get(s_name = name)
    # s_qs.s_name = name
    s_qs.s_major = major
    s_qs.s_age = age
    s_qs.s_grade = grade
    s_qs.s_gender = gender
    s_qs.save()
    return HttpResponseRedirect(reverse('search'))    

def student_delete(request, name):
    qs = Students.objects.get(s_name = name)
    qs.delete()
    return HttpResponseRedirect(reverse('search'))

