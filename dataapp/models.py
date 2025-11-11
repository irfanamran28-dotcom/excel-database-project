from django.db import models
from django.contrib.auth.models import User

class ExcelData(models.Model):
    column1 = models.CharField(max_length=200, blank=True, null=True)
    column2 = models.CharField(max_length=200, blank=True, null=True)
    column3 = models.TextField(blank=True, null=True)
    column4 = models.IntegerField(blank=True, null=True)
    column5 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    column6 = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='excel_data')
    
    class Meta:
        db_table = 'excel_data'
        verbose_name = 'Excel Data'
        verbose_name_plural = 'Excel Data Records'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.column1} - {self.id}"


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name