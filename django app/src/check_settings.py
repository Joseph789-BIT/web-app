import os
import sys
from django.conf import settings

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'showblit.settings'

# Import and set up Django
import django
django.setup()

# Now print the settings we're interested in
print("BASE_DIR:", settings.BASE_DIR)
print("STATIC_ROOT:", getattr(settings, 'STATIC_ROOT', 'Not set'))
print("STATIC_URL:", settings.STATIC_URL)