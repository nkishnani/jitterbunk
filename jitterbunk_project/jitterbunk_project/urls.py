from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^jitterbunk/', include('jitterbunk.urls', namespace='jitterbunk')),
    url(r'^admin/', include(admin.site.urls)),
]
