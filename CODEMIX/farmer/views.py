from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def farmerlogin(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        # aadhar = request.POST['aadhar']
        password=request.POST['password1']

        user = auth.authenticate(first_name=first_name,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Enter the correct password')
            return redirect('farmerlogin')
    else:
        return render(request,'farmerlogin.html')
def farmer(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        aadhar=request.POST['aadhar']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            user=User.objets.create_user(first_name=first_name,last_name=last_name,email=aadhar,password=password1)
            user.save()
            return redirect('farmerlogin')
    
        else:
            messages.info(request, 'Password not matching')
            return redirect('farmer')
        return redirect('/')
    else:
        return render(request,'farmer.html')