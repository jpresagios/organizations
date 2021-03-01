from django.core.management.base import BaseCommand, CommandError
from api.fake import generate_all
from organization.models import Organization, OrganizationMember
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Compute data for models'

    def handle(self, *args, **options):
        """
        Inserted some demo data
        """

        Organization.objects.all().delete()
        OrganizationMember.objects.all().delete()
        User.objects.all().delete()

        generate_all()

        self.stdout.write(self.style.SUCCESS("Succesfully, imported all data"))
