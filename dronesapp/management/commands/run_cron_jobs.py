from django.core.management.base import BaseCommand
from dronesapp.cronjobs import cron_job_handle

class Command(BaseCommand):
    help = 'Run cron job from console'

    def handle(self, *args, **options):
        cron_job_handle()
