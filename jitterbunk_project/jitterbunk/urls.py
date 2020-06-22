from django.conf.urls import url

from . import views

urlpatterns = [
    # /jitterbunk/
    url(r'^$', views.index, name='index'),
    # /jitterbunk/all/
    url(r'^all/?$', views.UserListView.as_view(), name='user-list'),
    # /jitterbunk/bunk/
    url(r'^bunk/', views.send_bunk, name='send_bunk'),
    # /jitterbunk/user/[username]
    url(r'^user/(?P<username>.*)$', views.view_individual_bunks, name='view_individual_bunks'),
]
