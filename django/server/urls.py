from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register(r'users', UserView, basename='users')

api_url_patterns = router.urls + []

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((api_url_patterns, 'api'), namespace='v1')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
