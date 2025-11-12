import os
import sys
import traceback

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

import django
from django.test import Client

try:
    django.setup()
    client = Client()

    # Try posting to the login URL. Adjust credentials if needed.
    print('Posting to /data/login/ ...')
    # Use HTTP_HOST header so Django doesn't raise DisallowedHost in test client
    response = client.post('/data/login/', {'username': 'admin', 'password': 'password'}, follow=True, HTTP_HOST='localhost')
    print('Status code:', response.status_code)
    print('Final URL:', response.request.get('PATH_INFO'))
    print('Response content (truncated):')
    print(response.content.decode('utf-8')[:4000])
except Exception as e:
    print('Exception occurred:')
    traceback.print_exc()
    sys.exit(1)
