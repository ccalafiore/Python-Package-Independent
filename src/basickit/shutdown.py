import os
from datetime import datetime


def if_time_is_out(year, month, day, hour=0, minute=0, second=0, microsecond=0, restart=False):

    time_out = datetime(year, month, day, hour=hour, minute=minute, second=second, microsecond=microsecond)
    time_now = datetime.now()
    time_is_out = time_out <= time_now
    if time_is_out:
        now(restart=restart)

    return time_is_out


def now(restart=False):

    if restart:
        # Do these commands only works on windows?
        os.system("shutdown /r /t 1")
    else:
        os.system("shutdown /s /t 1")
