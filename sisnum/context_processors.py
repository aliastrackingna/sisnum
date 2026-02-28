from django.conf import settings


def logo_context(request):
    return {
        'logo_url': settings.STATIC_URL + 'logo.png',
    }
