from django.contrib             import admin
from django.urls                import include, path
from django.conf.urls.static    import static
from django.conf.urls           import include, url
from django.conf                import settings

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
