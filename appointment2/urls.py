"""appointment2 URL Configuration

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
from django.urls import path,include
from base import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('DoctorApi',views.Doctor_data)
router.register('AppointmentApi',views.AppointmentData)
router.register('BillingApi',views.BillingData)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('c/', views.create_appointment, name='create_appointment'),
    # path('l/', views.list_appointments, name='list_appointments'),
    # path('cb/<int:appointment_id>/', views.create_bill, name='create_bill'),
]


