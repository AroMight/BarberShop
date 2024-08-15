from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls
from . import views

urlpatterns = [
    path('', views.HomeViewSet.as_view()),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
] + debug_toolbar_urls()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
