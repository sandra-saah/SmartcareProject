from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'smartcare/home.html')