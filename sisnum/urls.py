from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from documentos.views import index
from django.views.generic import TemplateView

handler400 = 'sisnum.views.bad_request'
handler403 = 'sisnum.views.permission_denied'
handler404 = 'sisnum.views.page_not_found'
handler500 = 'sisnum.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('documentos.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
