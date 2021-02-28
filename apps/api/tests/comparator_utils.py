from organization.models import OrganizationMember, Organization

def comparator_organization(org_model, org_dict):
    return org_model.phone == org_dict['phone'] and \
           org_model.name == org_dict['name'] and \
           org_model.address == org_dict['address']


def comparator_organization_members(organization, list_members_response):
    
    response_member_pk = [member['pk'] for member in list_members_response]
    
    # Every member response belong to members organization
    for member_response_id in response_member_pk:        
        is_member = OrganizationMember.objects.filter(organization=organization, pk=member_response_id).count()

        if is_member == 0:
            return False

    # Every member from organization is in the response members
    for member in organization.members.all():
        if member.pk not in response_member_pk:
            return False

    # Every member response is in Organization and every member from Organization in response
    # => then response contains exactly every member Organization
    return True


def comparator_member(member_model, member_dict):
    return member_model.name == member_dict['name'] and \
           member_model.phone == member_dict['phone'] and \
           member_model.organization.name == member_dict['organization_name']