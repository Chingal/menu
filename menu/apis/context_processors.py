from django.core.urlresolvers import reverse

def menu(request):
    print

    menu = {
        'opc': [
            {'name': 'Home', 'url' : reverse('index') },
            {'name': 'Add', 'url' : reverse('index') },
        ]
    }
    for i in menu['opc']:
        if request.path == i['url']:
            i['active'] = True
    print menu

    return menu