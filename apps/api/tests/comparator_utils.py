def comparate_organization(org_model, org_dict):
    return org_model.phone == org_dict['phone'] and \
           org_model.name == org_dict['name'] and \
           org_model.address == org_dict['address']
