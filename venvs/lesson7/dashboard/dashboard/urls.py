from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
