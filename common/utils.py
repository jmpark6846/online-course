import time
import random

import pendulum
from pendulum.datetime import DateTime
from django.conf import settings
# from iamporter import Iamporter

def get_now() -> DateTime:
    """Get current pendulum datetime instance of default timezone

    Returns:
        DateTime
    """
    return pendulum.now(settings.TIME_ZONE)


def generate_unique_id() -> str:
    """
    Time based unique_id Function
    {length: 14, unique_for: {years: 34}, time_resolution: 100ms}
    """
    return str((int(time.time() * 1000) & 0xffffffffff) * 100 + int(random.random() * 100))

#
# def get_iamport_client() -> Iamporter:
#     return Iamporter(imp_key=settings.IMP_REST_KEY, imp_secret=settings.IMP_REST_SECRET, imp_url=settings.IMP_URL)
