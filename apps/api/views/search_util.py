from django.db.models import Q

def get_search_conditions(request):
    """
    Search query parameters using Or Q
    Maybe a future improve is pass when used Or and when And From Django Settings
    """
    query = None

    search_fields = ['name', 'phone']

    for field in search_fields:
        field_value = request.query_params.get(field, None)
        
        if field_value:
            if query:
                query = query | Q((field,field_value))
            else:
                query = Q((field,field_value))
    
    email = request.query_params.get('email', None)

    if email and query:
        query = query | Q(('user__email', email))
    elif email:
        query= Q(('user__email', email))
        
    return query