from django.forms import ModelForm
from .models import SiteSettings


class SettingsForm(ModelForm):
    class Meta:
        model = SiteSettings
        fields = '__all__'
