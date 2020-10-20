from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('admin/', admin.site.urls),
    path('products/<int:product_id>/', views.product_detail_view, name="product_detail_view"),
    path('orders/<int:order_id>/',views.order_detail_view,name="order_detail_view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    """urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)"""
