from django.contrib import admin
from .models import Subject

# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_code', 'subject_name', 'instructor_name', 'created_at')
    list_filter = ('instructor_name', 'created_at')
    search_fields = ('subject_code', 'subject_name', 'instructor_name')
    ordering = ('subject_code',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('ข้อมูลวิชา', {
            'fields': ('subject_code', 'subject_name', 'instructor_name')
        }),
        ('ข้อมูลระบบ', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
