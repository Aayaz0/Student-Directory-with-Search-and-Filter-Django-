from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'student_id', 'department', 'parent_name', 'parent_phone']
    list_filter = ['department']
    search_fields = ['name', 'student_id', 'department', 'parent_name', 'parent_phone']
    ordering = ['student_id']
