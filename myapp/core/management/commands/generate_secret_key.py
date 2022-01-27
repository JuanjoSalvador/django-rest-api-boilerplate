from django.core.management import utils
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generates a new SECRET KEY for your project.'

    def handle(self, *args, **kwargs):
        print("KEEP IT SECRET ON PRODUCTION!\n")
        print(f"Your new key is: {utils.get_random_secret_key()}")