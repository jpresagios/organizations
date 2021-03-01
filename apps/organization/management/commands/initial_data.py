from django.core.management.base import BaseCommand, CommandError
from api.fake import generate_all


class Command(BaseCommand):
    help = 'Compute data for models'

    def handle(self, *args, **options):
        """
        Inserted some demo data
        """

        generate_all()

        self.stdout.write(self.style.SUCCESS("Succesfully, imported all data"))
