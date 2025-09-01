from django.db import models

# Create your models here.

class Subject(models.Model):
    subject_code = models.CharField(max_length=10, unique=True, verbose_name="รหัสวิชา")
    subject_name = models.CharField(max_length=200, verbose_name="ชื่อวิชา")
    instructor_name = models.CharField(max_length=100, verbose_name="ชื่อผู้สอน")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่อัปเดต")

    class Meta:
        verbose_name = "วิชา"
        verbose_name_plural = "วิชา"
        ordering = ['subject_code']

    def __str__(self):
        return f"{self.subject_code} - {self.subject_name}"

