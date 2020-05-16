from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('forms/', views.form_view, name="form_view"),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:slug>/',views.blog_view,name="blog_view"),
    path('homeworks/', views.homeworks_view, name="homeworks_view"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
