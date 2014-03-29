from django.shortcuts import render

# Create your views here.
def instascribe(request):
    return render(request, 'instascribe.html', {})