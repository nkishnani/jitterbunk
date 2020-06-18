from django.conf.urls import url

from . import views

urlpatterns = [
    # /jitterbunk/
    url(r'^$', views.index, name='index'),
    # /jitterbunk/bunk/
    url(r'^bunk/', views.send_bunk, name='send_bunk'),
    # /jitterbunk/user/[username]
    url(r'^user/(?P<username>.*)$', views.view_individual_bunks, name='view_individual_bunks'),
]
