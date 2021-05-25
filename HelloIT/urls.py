"""HelloIT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django_registration.backends.one_step.views import RegistrationView

from users.forms import CustomUserForm

urlpatterns = [
    path('admin/', admin.site.urls),

    # Custom registration view
    path('accounts/register',
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url="/",
         ), name="django_registration_register"),

    # urls used by django-registration
    path('accounts/',
         include('django_registration.backends.one_step.urls')),

    # Login urls provided by django
    path('accounts/',
         include('django.contrib.auth.urls')),

    # Login via browsable API
    path('api-auth/',
         include("rest_framework.urls")),

    # login via REST
    path('api/rest-auth/',
         include('rest_auth.urls ')),

    # register via REST
    path('api/rest-auth/registration/',
         include('rest_auth.registration.urls'))
]
