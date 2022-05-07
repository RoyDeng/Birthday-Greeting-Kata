import subprocess
from os.path import join

from django.core.management import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = "Deploy PBN"

    def handle(self, *args, **kw):
        # cronjob
        subprocess.call(['python', 'manage.py', 'crontab', 'remove'])
        subprocess.call(['python', 'manage.py', 'crontab', 'add'])
        subprocess.call(['touch', '/var/log/cron.log'])
        subprocess.call(['service', 'cron', 'restart'])
        subprocess.call(["supervisorctl", "restart", "all"])
        self.stdout.write("Finish deploying!")
        subprocess.call(["/usr/bin/supervisord"])
