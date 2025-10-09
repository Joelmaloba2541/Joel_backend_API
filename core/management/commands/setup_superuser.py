from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Run migrations and create superuser if it does not exist'

    def handle(self, *args, **options):
        # Run migrations
        self.stdout.write('Running migrations...')
        call_command('migrate')

        # Check and create superuser
        if not User.objects.filter(username='admin').exists():
            self.stdout.write('Creating superuser...')
            User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')
            self.stdout.write('Superuser created successfully.')
        else:
            self.stdout.write('Superuser already exists.')
