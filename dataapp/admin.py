from django.contrib import admin
from .models import ExcelData

@admin.register(ExcelData)
class ExcelDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'column1', 'column2', 'column3','created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['column1', 'column2', 'column3']
    list_per_page = 50
    
    # Add export functionality
    actions = ['export_as_csv']
    
    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['ID', 'Column1', 'Column2', 'Column3', 'created_at'])
        
        for obj in queryset:
            writer.writerow([obj.id, obj.column1, obj.column2, obj.column3, obj.created_at])
        
        return response
    
    export_as_csv.short_description = "Export Selected to CSV"