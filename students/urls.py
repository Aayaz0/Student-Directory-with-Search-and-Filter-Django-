from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_students, name='search_students'),
    path('api/students/', views.StudentListAPI.as_view(), name='student_api'),
]
