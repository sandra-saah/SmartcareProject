"""SmartcareProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from accounts import views
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home_view,name=''),

    path('adminclick', views.adminclick_view),
    path('doctorclick', views.doctorclick_view),
    path('patientclick', views.patientclick_view),
    path('nurseclick', views.nurseclick_view),

    path('adminsignup', views.admin_signup_view),
    # path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    # path('nursesignup', views.nurse_signup_view, name="nursesignup"),
    # path('patientsignup', views.patient_signup_view),

    path('adminlogin', LoginView.as_view(template_name='smartcare/adminlogin.html')),
    path('doctorlogin', LoginView.as_view(template_name='smartcare/doctorlogin.html')),
    path('doctorlogin', LoginView.as_view(template_name='smartcare/nurselogin.html')),
    path('patientlogin', LoginView.as_view(template_name='smartcare/patientlogin.html')),

    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='smartcare/home.html'),name='logout'),

    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
]
