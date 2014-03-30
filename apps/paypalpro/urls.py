from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'apps.paypalpro.views.buy_item', name='buy_item'),
    url(r'^success/$', 'apps.paypalpro.views.success', name='success'),
    (r'^ipn/', include('paypal.standard.ipn.urls')),
    (r'^pdt/', include('paypal.standard.pdt.urls')),
)
