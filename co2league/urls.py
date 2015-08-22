from django.conf.urls import patterns,include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tco.views.first_screen', name='first_screen'),
    url(r'^home', 'tco.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^main', 'tco.views.main', name='main'),
    url(r'^about-us/', 'tco.views.aboutus', name='aboutus'),
    url(r'^housing', 'tco.views.housing', name='housing'),
    url(r'^travel', 'tco.views.travel', name='travel'),
    url(r'^food', 'tco.views.food', name='food'),
    url(r'^shopping', 'tco.views.shopping', name='shopping'),
    url(r'^oauth_callback', 'tco.views.user_start', name='user_start'),
    url(r'^first_screen', 'tco.views.first_screen', name='first_screen'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
		document_root = settings.STATIC_ROOT)

	urlpatterns += static(settings.MEDIA_URL,
		document_root = settings.MEDIA_ROOT)
