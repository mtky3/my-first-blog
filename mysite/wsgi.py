"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

import sys
#
## assuming your django settings file is at '/home/nokkun/mysite/mysite/settings.py'
## and your manage.py is is at '/home/nokkun/mysite/manage.py'
path = '/home/mtky3/my-first-blog'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
