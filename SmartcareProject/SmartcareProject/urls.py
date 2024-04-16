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
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    # path('nursesignup', views.nurse_signup_view, name="nursesignup"),
    # path('patientsignup', views.patient_signup_view),

    path('adminlogin', LoginView.as_view(template_name='smartcare/adminlogin.html')),
    path('doctorlogin', LoginView.as_view(template_name='smartcare/doctorlogin.html')),
    path('nurselogin', LoginView.as_view(template_name='smartcare/nurselogin.html')),
    path('patientlogin', LoginView.as_view(template_name='smartcare/patientlogin.html')),

    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='smartcare/home.html'),name='logout'),

    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    # admin dotor links 
    path('admin-doctor', views.admin_doctor_view,name='admin-doctor'),
    path('admin-view-doctor', views.admin_view_doctor_view,name='admin-view-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),
    path('admin-add-doctor', views.admin_add_doctor_view,name='admin-add-doctor'),
    path('admin-approve-doctor', views.admin_approve_doctor_view,name='admin-approve-doctor'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name='reject-doctor'),
    # path('admin-view-doctor-specialisation',views.admin_view_doctor_specialisation_view,name='admin-view-doctor-specialisation'),

    # admin appointment links 
    path('admin-appointment', views.admin_appointment_view,name='admin-appointment'),
    path('admin-view-appointment', views.admin_view_appointment_view,name='admin-view-appointment'),
    path('admin-add-appointment', views.admin_add_appointment_view,name='admin-add-appointment'),
    path('admin-approve-appointment', views.admin_approve_appointment_view,name='admin-approve-appointment'),


]

# Doctor related links 

urlpatterns +=[
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),

    path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient_view,name='doctor-view-patient'),
    path('doctor-view-discharge-patient',views.doctor_view_discharge_patient_view,name='doctor-view-discharge-patient'),

    path('doctor-appointment', views.doctor_appointment_view,name='doctor-appointment'),
    path('doctor-view-appointment', views.doctor_view_appointment_view,name='doctor-view-appointment'),
    path('doctor-delete-appointment',views.doctor_delete_appointment_view,name='doctor-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view,name='delete-appointment'),


    ]
