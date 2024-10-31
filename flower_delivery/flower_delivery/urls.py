# flower_delivery/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    # User registration and authentication
    path('users/', include('users.urls')),  # Routes for registration, login, logout

    # Flower catalog routes
    path('flower_catalog/', include('flower_catalog.urls', namespace='flower_catalog')),  # Catalog viewing

    # Order creation and management
    path('orders/', include('orders.urls', namespace='orders')),  # Order form and details

    # Redirect root URL to catalog page
    path('', RedirectView.as_view(url='/flower_catalog/', permanent=True)),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

