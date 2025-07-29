from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student
from rest_framework import generics
from .serializers import StudentSerializer
from django.db.models import Q

# Create your views here.

@login_required
def index(request):
    return render(request, 'students/index.html')

@login_required
def search_students(request):
    query = request.GET.get('q', '')
    students = Student.objects.filter(
        Q(name__icontains=query) | Q(student_id__icontains=query) | Q(department__icontains=query)
    ) if query else []
    return render(request, 'students/search_results.html', {'students': students, 'query': query})

class StudentListAPI(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
