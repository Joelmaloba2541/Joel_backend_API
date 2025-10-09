from django.core.management.commands.runserver import Command as BaseRunserverCommand
from django.core.management import call_command
from django.contrib.auth.models import User

class Command(BaseRunserverCommand):
    def handle(self, *args, **options):
        # Run migrations
        self.stdout.write('Running migrations...')
        call_command('migrate')

        # Check and create superuser
        if not User.objects.filter(username='admin').exists():
            self.stdout.write('Creating superuser...')
            User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')
        else:
            self.stdout.write('Superuser already exists.')

        # Now run the server
        super().handle(*args, **options)
