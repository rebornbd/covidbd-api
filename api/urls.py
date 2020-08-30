
from . import views
from django.urls import path

# TEMPLATE TAGGING
app_name = 'bdcovidapi'

urlpatterns = [
    path('', views.home, name='home'),
    path('districts', views.getDistrictData, name='districts'),
    path('divisions', views.getDivisionData, name='divisions'),
    path('status', views.getStatus, name='status'),
    path('about', views.about, name='about')
]
