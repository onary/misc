from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.conf import settings

from paypal.pro.views import PayPalPro

def buy_item(request):
    item = {"amt": "10.00",                 # amount to charge for item
        "inv": "inventory",                 # unique tracking variable paypal
        "custom": "tracking",               # custom tracking variable for you
        "cancelurl": settings.SITE_URL,     # Express checkout cancel url
        "returnurl": reverse('buy_item')    # Express checkout return url
        }

    kw = {"item": item,                          # what you're selling
        "payment_template": "payment.html",      # template name for payment
        "confirm_template": "confirmation.html", # template name for confirmation
        "success_url": reverse('success')}       # redirect location after success

    ppp = PayPalPro(**kw)
    return ppp(request)

def success(request):
    return render(request, 'success.html', {})