# gym_ua_django/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bdd_gym_ua/', include('bdd_gym_ua.urls')),
    path('', RedirectView.as_view(url='/bdd_gym_ua/alumnos/', permanent=True)),
]
