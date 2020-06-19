from django.shortcuts import render, get_object_or_404
from siteinfo.models import SiteSettings

# Create your views here.
def index(request):
    general_info = get_object_or_404(SiteSettings, pk=1)
    context = {
        'site_info': general_info,
    }
    return render(request, 'products/index.html', context)
