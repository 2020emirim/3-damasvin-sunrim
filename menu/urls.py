from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
app_name = 'menu'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('menu.urls')),
    path('order/', include('order.urls')),
    path('', include('order.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)