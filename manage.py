#!/usr/bin/env python
import os
import sys

from dotenv import load_dotenv, find_dotenv

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

    try:
        load_dotenv(find_dotenv())
        print(".env 불러오기")
    except:
        print(".env 불러오기 실패")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
