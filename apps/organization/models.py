from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True


class Organization(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    phone = models.CharField(_("Phone"), max_length=50)
    address = models.TextField(_("Address"))

    def __str__(self):
        return self.name


class OrganizationMember(models.Model):
    """
    Represent a User that belong to an Organization
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='organization_member')
    name = models.CharField(_("Name"), max_length=100)
    phone = models.CharField(_("Phone"), max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='members')
    birthdate = models.DateField(_('Birthdate'))

    def __str__(self):
        return f"{self.name}, {self.organization}"
