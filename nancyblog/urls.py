import os

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from wagtail.contrib.wagtailsitemaps.views import sitemap
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailsearch import urls as wagtailsearch_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtailimages import urls as wagtailimages_urls


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^search/', include(wagtailsearch_urls)),
    url(r'^images/', include(wagtailimages_urls)),
    url('^sitemap\.xml$', sitemap),

    url(r'', include(wagtail_urls)),
)


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
