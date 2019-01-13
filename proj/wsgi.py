"""
WSGI config for proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv, find_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

try:
    load_dotenv(find_dotenv())
    print(".env 불러오기")
except:
    print(".env 불러오기 실패")

application = get_wsgi_application()
