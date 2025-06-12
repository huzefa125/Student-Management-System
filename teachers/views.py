from django.shortcuts import render

# Create your views here.

def teachers_list(request):
    return render(request, 'teachers.html')
