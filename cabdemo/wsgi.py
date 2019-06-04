"""
WSGI config for cabdemo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/var/www/html/cabdemo/cabdemo')
sys.path.append('/var/www/html/cabdemo/cabdemo_env')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabdemo.settings.production')

application = get_wsgi_application()

