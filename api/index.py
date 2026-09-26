import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

import django
django.setup()

from django.core.management import call_command

# Static files collect
call_command("collectstatic", interactive=False, verbosity=0)

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()