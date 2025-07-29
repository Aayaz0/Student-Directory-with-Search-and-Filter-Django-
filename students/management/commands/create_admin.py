from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create admin user for production'

    def handle(self, *args, **options):
        # Create superuser if doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write('Superuser "admin" created with password "admin123"')
        else:
            self.stdout.write('Superuser "admin" already exists')
            
        # Print all existing users for debugging
        users = User.objects.all()
        self.stdout.write(f'Total users in database: {users.count()}')
        for user in users:
            self.stdout.write(f'User: {user.username} (is_superuser: {user.is_superuser})')
