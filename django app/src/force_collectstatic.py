import os
import django
from django.core.management import call_command

os.environ['DJANGO_SETTINGS_MODULE'] = 'showblit.settings'
django.setup()

from django.conf import settings

# Force set STATIC_ROOT
settings.STATIC_ROOT = r'C:\Users\USER\Desktop\100 Code\work\web-app\django app\staticfiles'

print("Forced STATIC_ROOT:", settings.STATIC_ROOT)

# Run collectstatic
call_command('collectstatic', interactive=False, verbosity=2)
