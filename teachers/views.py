from django.shortcuts import render
from .models import Teacher

# Create your views here.

def teachers(request):
    teachers_list = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers_list})
