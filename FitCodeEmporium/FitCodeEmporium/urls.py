from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),  # Includes URLs from the store app
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),  # Redirect for favicon
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
