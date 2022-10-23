from os import stat
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from tomlkit import document

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
