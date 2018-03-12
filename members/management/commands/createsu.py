from django.conf import settings
from django.core.management import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

# manage.py 액션을 추가하기 위해서

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username=settings.SUPERUSER_USERNAME).exists():
            User.objects.create_superuser(
                username=settings.SUPERUSER_USERNAME,
                password=settings.SUPERUSER_PASSWORD,
                email=settings.SUPERUSER_EMAIL,
            )
