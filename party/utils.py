def getRoutes(request):
    routes = [
        {
            'Endpoint': '/parties/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of all parties'
        },
        {
            'Endpoint': '/parties/<id>',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single party'
        },
        {
            'Endpoint': '/parties/create',
            'method': 'POST',
            'body': {'body': 'String'},
            'description': 'Creates a new party'
        },
        {
            'Endpoint': '/parties/<id>/update',
            'method': 'PUT',
            'body': {'body': 'String'},
            'description': 'Updates a party'
        },
        {
            'Endpoint': '/parties/<id>/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a party'
        },
    ]
    return routes