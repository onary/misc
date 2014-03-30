from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'apps.main.views.main', name='main'),
    url(r'^instascribe/$', 'apps.instascribe.views.instascribe', name='instascribe'),
    
    (r'^paypalpro/', include('apps.paypalpro.urls')),
    (r'^paypalpro/ipn/', include('paypal.standard.ipn.urls')),
    (r'^paypalpro/pdt/', include('paypal.standard.pdt.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
