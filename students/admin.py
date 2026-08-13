
from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "field", "gender", "email")
    search_fields = ("id", "name", "email")
    list_filter = ("field",)

