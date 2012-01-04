from django_cron import cronScheduler, Job
from frontend.views import *

class sendMail(Job):
    run_every = 60

    def job(self):
        cron_email()

cronScheduler.register(sendMail)
