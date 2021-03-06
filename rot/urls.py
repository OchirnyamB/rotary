from django.conf.urls.defaults import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from forums import views
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^$', RedirectView.as_view(url="/cms/")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cms/', include('cms.urls')),
    url(r'^forums/', include('forums.urls')),
    (r'^tinymce/', include('tinymce.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
