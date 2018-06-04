"""plakadan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from plakadan import settings
from plates import views as plates_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', plates_views.index, name='index'),
    path('logout/', plates_views.logout_view, name='logout'),
    path('add-plate/', plates_views.add_plate, name='add-plate'),
    path('call/<slug:plate_number>/', plates_views.call, name='call'),
    path('login-control/', plates_views.login_controller, name='login-controller'),
    path('register-control/', plates_views.register_controller, name='register-controller'),
    path('profile-update-control/', plates_views.profile_update_controller, name='profile-update-controller'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
