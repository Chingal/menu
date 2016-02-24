from django.conf.urls import patterns, url
from .views import MenuListView

urlpatterns = patterns('',
    url(r'^$',
        'django.contrib.auth.views.login',
        {'template_name': 'init/index.html'},
        name = "index"),

    url(r'^/$',
        MenuListView.as_view(),
        name = "listmenu"),

    url(r'^logout/$',
        'django.contrib.auth.views.logout_then_login',
        name =  "logout"),

)