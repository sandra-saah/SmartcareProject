from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from . import forms,models
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test


# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'smartcare/home.html')

#for showing signup/login button for admin
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'smartcare/adminclick.html')


#for showing signup/login button for doctor
def doctorclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'smartcare/doctorclick.html')


#for showing signup/login button for patient
def patientclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'smartcare/patientclick.html')

#for showing signup/login button for patient
def nurseclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'smartcare/nurseclick.html')

def admin_signup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
    return render(request,'smartcare/adminsignup.html',{'form':form})


def doctor_signup_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor=doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('doctorlogin')
    return render(request,'smartcare/doctorsignup.html',context=mydict)




#-----------for checking user is doctor , patient, nurse or admin
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_nurse(user):
    return user.groups.filter(name='NURSE').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()


#---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,DOCTOR, NURSE OR PATIENT

def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_doctor(request.user):
        accountapproval=models.Doctor.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('doctor-dashboard')
        else:
            return render(request,'smartcare/doctor_wait_for_approval.html')
    
    elif is_nurse(request.user):
        accountapproval=models.Nurse.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('nurse-dashboard')
        else:
            return render(request,'smartcare/nurse_wait_for_approval.html')

    elif is_patient(request.user):
        accountapproval=models.Patient.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('patient-dashboard')
        else:
            return render(request,'smartcare/patient_wait_for_approval.html')


#---------------------------------------------------------------------------------
#------------------------ ADMIN VIEWS  ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    #for both table in admin dashboard
    doctors=models.Doctor.objects.all().order_by('-id')
    # patients=models.Patient.objects.all().order_by('-id')
    #for three cards
    doctorcount=models.Doctor.objects.all().filter(status=True).count()
    pendingdoctorcount=models.Doctor.objects.all().filter(status=False).count()

    # patientcount=models.Patient.objects.all().filter(status=True).count()
    # pendingpatientcount=models.Patient.objects.all().filter(status=False).count()

    # appointmentcount=models.Appointment.objects.all().filter(status=True).count()
    # pendingappointmentcount=models.Appointment.objects.all().filter(status=False).count()
    mydict={
    'doctors':doctors,
    # 'patients':patients,
    'doctorcount':doctorcount,
    'pendingdoctorcount':pendingdoctorcount,
    # 'patientcount':patientcount,
    # 'pendingpatientcount':pendingpatientcount,
    # 'appointmentcount':appointmentcount,
    # 'pendingappointmentcount':pendingappointmentcount,
    }
    return render(request,'smartcare/admin_dashboard.html')

# this view for sidebar click on admin page
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_doctor_view(request):
    return render(request,'smartcare/admin_doctor.html')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_doctor_view(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    return render(request,'smartcare/admin_view_doctor.html',{'doctors':doctors})

# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def delete_doctor_from_hospital_view(request,pk):
#     doctor=models.Doctor.objects.get(id=pk)
#     user=models.User.objects.get(id=doctor.user_id)
#     user.delete()
#     doctor.delete()
#     return redirect('admin-view-doctor')



# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def update_doctor_view(request,pk):
#     doctor=models.Doctor.objects.get(id=pk)
#     user=models.User.objects.get(id=doctor.user_id)

#     userForm=forms.DoctorUserForm(instance=user)
#     doctorForm=forms.DoctorForm(request.FILES,instance=doctor)
#     mydict={'userForm':userForm,'doctorForm':doctorForm}
#     if request.method=='POST':
#         userForm=forms.DoctorUserForm(request.POST,instance=user)
#         doctorForm=forms.DoctorForm(request.POST,request.FILES,instance=doctor)
#         if userForm.is_valid() and doctorForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()
#             doctor=doctorForm.save(commit=False)
#             doctor.status=True
#             doctor.save()
#             return redirect('admin-view-doctor')
#     return render(request,'hospital/admin_update_doctor.html',context=mydict)



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_doctor_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST, request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor.status=True
            doctor.save()

            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)

        return HttpResponseRedirect('admin-view-doctor')
    return render(request,'smartcare/admin_add_doctor.html',context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_doctor_view(request):
    #those whose approval are needed
    doctors=models.Doctor.objects.all().filter(status=False)
    return render(request,'smartcare/admin_approve_doctor.html',{'doctors':doctors})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_doctor_view(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    doctor.status=True
    doctor.save()
    return redirect(reverse('admin-approve-doctor'))


#---------------------------------------------------------------------------------
#------------------------ DOCTOR RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_dashboard_view(request):
    #for three cards
    # patientcount=models.Patient.objects.all().filter(status=True,assignedDoctorId=request.user.id).count()
    # appointmentcount=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).count()
    # patientdischarged=models.PatientDischargeDetails.objects.all().distinct().filter(assignedDoctorName=request.user.first_name).count()

    #for  table in doctor dashboard
    # appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).order_by('-id')
    # patientid=[]
    # for a in appointments:
        # patientid.append(a.patientId)
    # patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid).order_by('-id')
    # appointments=zip(appointments,patients)
    mydict={
    # 'patientcount':patientcount,
    # 'appointmentcount':appointmentcount,
    # 'patientdischarged':patientdischarged,
    # 'appointments':appointments,
    # 'doctor':models.Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    }
    return render(request,'smartcare/doctor_dashboard.html',context=mydict)

