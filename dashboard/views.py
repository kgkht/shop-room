from django.shortcuts import render
from django.contrib.auth import decorators

# Create your views here.
@decorators.login_required
def index(request):
    return render(request, 'dashboard/index.html')


from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from siteinfo.models import SiteSettings

class SiteSettingsUpdateView(LoginRequiredMixin, UpdateView):

    model = SiteSettings
    fields = '__all__'
    template_name = 'dashboard/sitesettings_update_form.html'
    
