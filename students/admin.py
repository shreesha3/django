from django.contrib import admin
from import_export.admin import ExportMixin
from .models import Student  # Adjust if your model is in a different location

class StudentAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('name', 'percentage')  # Replace with your actual field names

admin.site.register(Student,StudentAdmin)
