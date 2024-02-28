from django.shortcuts import render
from django.http import HttpResponse
from .models import Students

# Create your views here.
def index(request):
    # return HttpResponse("Web Development Schoolapp")
    students = Students.objects.all() # SELECT * FROM students
    context = {"students": students}

    return render(request, 'school/index.html', context)