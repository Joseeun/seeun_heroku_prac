from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserInformation, UserInformationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        form2=UserInformationForm(request.POST)
        if form.is_valid() and form2.is_valid():
            user=form.save()
            user_information = form2.save(commit=False)
            user_information.user = user
            user_information.save()
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'account/signup.html', {'form':form, 'form2':form2})
        
    else:
        form=UserCreationForm()
        form2=UserInformationForm()
        return render(request, 'account/signup.html', {'form':form, 'form2':form2})

def login(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            auth.login(request,user)
            return redirect('main')
        else:
            return render(request, 'account/login.html', {'form':form})
    else:
        form=AuthenticationForm()
        return render(request,'account/login.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('main')

