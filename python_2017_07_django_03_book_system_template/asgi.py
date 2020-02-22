"""
ASGI config for python_2017_07_django_03_book_system_template project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_2017_07_django_03_book_system_template.settings')

application = get_asgi_application()
