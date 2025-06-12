from django.shortcuts import render

# Create your views here.

def classes_list(request):
    return render(request, 'classes.html')
