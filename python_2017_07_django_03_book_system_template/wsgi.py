"""
WSGI config for python_2017_07_django_03_book_system_template project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_2017_07_django_03_book_system_template.settings')

application = get_wsgi_application()
