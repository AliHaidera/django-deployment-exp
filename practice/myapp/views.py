from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.forms import userform,userinfoform



def index(request):
    return render(request,'myapp/index.html')

def register(request):

    registered=False
    if request.method=="POST":
        userfo=userform(request.POST)
        profilefo=userinfoform(request.POST)

        if userfo.is_valid() and profilefo.is_valid():
            user=userfo.save()
            user.set_password(user.password)
            user.save()
            profile=profilefo.save(commit=False)
            profile.user=user
            if 'picture' in request.FILES:
                profile.picture=request.FILES['picture']
                profile.save()
                registered=True
            else:
                print(user.errors,profile.errors)
    else:
            userfo=userform()
            profilefo=userinfoform()

    return render(request,'myapp/register.html',{'userfo':userfo,'profilefo':profilefo,"registered":registered})

def loginpage(request):

    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print("user is not active")
        else:
            print("not provide the valid info ")

    return render(request,'myapp/loginpage.html',{})


@login_required
def logoutpage(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
