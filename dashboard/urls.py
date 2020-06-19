from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('settings/<int:pk>/update', views.SiteSettingsUpdateView.as_view(), name='site-settings'),
]
