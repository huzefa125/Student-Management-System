from django.shortcuts import render

# Create your views here.

def attendance_list(request):
    return render(request, 'attendance.html')
