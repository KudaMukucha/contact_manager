from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout,update_session_auth_hash
from .forms import UpdateProfileForm,SignUpForm
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
#login users
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username =username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                messages.success(request,f'You have logged in as {user}')
                return redirect('dashboard')
            else:
                return redirect('account-block')
        else:
            messages.warning(request,'Invalid username or password!')
            return render(request,'accounts/login.html',{'username':username})
    else:
         return render(request,'accounts/login.html')
    

#logout users
def logout_user(request):
    logout(request)
    messages.success(request,'Your active session has ended. Please log in to continue.')
    return redirect('login')

#update info
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile is now updated!')
            return redirect('home')
        else:
            messages.warning(request,'Oops, something went wrong! Please try again.')
            return redirect('update-profile')
    else:
        form = UpdateProfileForm(instance=request.user)
        return render(request,'accounts/update-profile.html',{'form':form})

#change password
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Password changed successfully.')
            return redirect('home')
        else:
            messages.warning(request,'Oops, something went wrong. Please check password.')
            return render(request,'accounts/change-password.html',{'form':form})
    else:
        form = PasswordChangeForm(request.user)
        return render(request,'accounts/change-password.html',{'form':form})
    

#account block
def account_block(request):
    return render(request,'accounts/account-block.html')


#register users
def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,'You have successfully registered...')
            return redirect('dashboard')
    return render(request,'accounts/register.html',{'form':form})
