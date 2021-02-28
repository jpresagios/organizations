# This file contains fake data for testing purpose and for
# initial database population


from faker import Faker
from django.contrib.auth.models import User, Group
from organization.models import OrganizationMember, Organization
from api.auth_groups import get_auth_groups
import random
import datetime

faker = Faker()


def add_user_to_group(user, group_name=None):
    groups = get_auth_groups()

    if group_name:
        group, _ = Group.objects.get_or_create(name=group_name)
    else:
        group, _ = Group.objects.get_or_create(name=groups[random.randint(0, len(groups) - 1)])

    group.user_set.add(user)


def gen_users(numbers=10):
    user_list = []

    # Should be at less 3 user in each auth group
    groups = get_auth_groups()

    for group in groups:
        email = faker.email()
        user = User.objects.create_superuser(email, email, 'admin123')
        add_user_to_group(user, group)

    count_groups = len(groups)
    for i in range(numbers - count_groups):
        email = faker.email()
        user = User.objects.create_superuser(email, email, 'admin123')
        add_user_to_group(user)
        user_list.append(user)

    return user_list


def gen_organizations(numbers=2):
    organization_list = []

    for i in range(numbers + 1):
        organization, _ = Organization.objects.get_or_create(name=faker.name(),
                                                             phone=faker.phone_number(),
                                                             address=faker.address())

        organization_list.append(organization)

    return organization_list


def gen_organization_members():
    organization_list = []

    organizations = Organization.objects.all()
    count_organizations = organizations.count()

    for user in User.objects.all():
        org = organizations[random.randint(0, count_organizations - 1)]

        member, _ = OrganizationMember.objects.get_or_create(user=user,
                                                             name=faker.name(),
                                                             phone=faker.phone_number(),
                                                             organization=org,
                                                             birthdate=datetime.datetime.now())


def generate_all():
    gen_users()
    gen_organizations()
    gen_organization_members()
