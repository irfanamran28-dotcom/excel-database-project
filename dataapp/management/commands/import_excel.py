# Save this as: dataapp/management/commands/import_excel.py

from django.core.management.base import BaseCommand
import pandas as pd
from dataapp.models import ExcelData
from datetime import datetime

class Command(BaseCommand):
    help = 'Import data from Excel file'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Path to Excel file')

    def handle(self, *args, **kwargs):
        excel_file = kwargs['excel_file']
        
        self.stdout.write(self.style.SUCCESS(f'Reading Excel file: {excel_file}'))
        
        try:
            # Read Excel file
            df = pd.read_excel(excel_file)
            
            self.stdout.write(f'Found {len(df)} rows')
            self.stdout.write(f'Columns: {", ".join(df.columns.tolist())}')
            
            # Show first few column names to help with mapping
            self.stdout.write(self.style.WARNING('\nFirst 3 rows of data:'))
            self.stdout.write(str(df.head(3)))
            
            records_created = 0
            records_failed = 0
            
            for index, row in df.iterrows():
                try:
                    # IMPORTANT: Adjust these field mappings to match your Excel columns
                    # Print the first row to see what columns you have
                    if index == 0:
                        self.stdout.write(self.style.WARNING(f'\nAvailable columns in Excel: {list(row.keys())}'))
                    
                    # Map your Excel columns to model fields
                    # Change the column names below to match YOUR Excel file
                    ExcelData.objects.create(
                        column1=str(row.get(df.columns[0], ''))[:200],  # First column
                        column2=str(row.get(df.columns[1], ''))[:200] if len(df.columns) > 1 else '',  # Second column
                        column3=str(row.get(df.columns[2], '')) if len(df.columns) > 2 else '',  # Third column
                        column4=int(row.get(df.columns[3], 0)) if len(df.columns) > 3 and pd.notna(row.get(df.columns[3])) else None,  # Fourth column
                        column5=float(row.get(df.columns[4], 0)) if len(df.columns) > 4 and pd.notna(row.get(df.columns[4])) else None,  # Fifth column
                        column6=pd.to_datetime(row.get(df.columns[5], None), errors='coerce') if len(df.columns) > 5 else None,  # Sixth column
                    )
                    records_created += 1
                    
                    if records_created % 100 == 0:
                        self.stdout.write(f'Processed {records_created} records...')
                        
                except Exception as e:
                    records_failed += 1
                    self.stdout.write(
                        self.style.ERROR(f'Error at row {index + 2}: {str(e)}')  # +2 because Excel rows start at 1 and have header
                    )
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'\n{"="*50}\n'
                    f'Import completed!\n'
                    f'Records created: {records_created}\n'
                    f'Records failed: {records_failed}\n'
                    f'{"="*50}'
                )
            )
            
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f'File not found: {excel_file}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Failed to read Excel file: {str(e)}')
            )