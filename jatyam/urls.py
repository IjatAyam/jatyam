from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_tools/', include('admin_tools.urls')),
    path('martor/', include('martor.urls')),
    path('contact/', include('account.urls')),
    path('showcase/', include('skill.urls')),
    path('blog/', include('blog.urls')),
    path('', include('personal.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
