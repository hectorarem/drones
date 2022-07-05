import time
from .tasks import update_drone_battery


def cron_job_handle():
    time.sleep(60) # ich 5 min
    print(bcolors.OKCYAN + "cron jobs started")
    try:
        update_drone_battery()
        print(bcolors.OKGREEN + "cron jobs executed")
        return cron_job_handle()
    except:
        print(bcolors.FAIL + "Error! executing the cron job, please check your code!")
        # todo send emails to devs
        return cron_job_handle()

class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'