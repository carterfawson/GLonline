"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from django.views.generic import *
from app.forms import BootstrapAuthenticationForm

from app.views import *
from app.forms import *
# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^customers', 'app.views.customers', name='customers'),
    url(r'^customer/(?P<custid_url>[\w\d/+/%\s]+)/$', 'app.views.customer_specific', name='customer'),
    url(r'^job/([\w\d/+]+)/([\w\d/+]+)/$', 'app.views.job_specific', name='job'),
    url(r'^invoice/([\w\d/+]+)/([\w\d/+]+)/$', 'app.views.inv_specific', name='invoice'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
