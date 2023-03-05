
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('admin/', admin.site.urls),
    path('api/', include('party.urls')),
    path('accounts/', include('accounts.api.urls')),
    re_path('', TemplateView.as_view(template_name='index.html')),
]  
