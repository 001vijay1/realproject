from django.shortcuts import render, redirect
import random
from .models import UserProfile, Users
from .forms import UserForm, LoginForm, ChangePasswordForm, ResetPasswordForm, NewPasswordForm
from django.contrib import messages


# Create your views here.
def user_register(request):
    if request.session.get('email', None):
        return redirect('dashboard')

    if 'otp_code' in request.POST:
        in_otp = request.POST.get('otp_code')
        ses_key = request.session['opt_gen']
        uname = request.session.get('username')
        psw = request.session.get('password')
        eml = request.session.get('signup_email')
        mob = request.session.get('mobile')

        print(in_otp, type(in_otp), ses_key, type(ses_key))
        if int(in_otp) == int(ses_key):

            signup = Users(username=uname, password=psw, email=eml, mobile=mob)
            signup.save()

            print('Form Submitted')
            return redirect('login')

        else:
            context = {
                'mes': 'Your Otp Not Match..',

            }
            return render(request, 'opt.html', context)
    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        mobile = form.cleaned_data.get('mobile')
        # print(username,password,email)
        opt_gen = random.randrange(111111, 999999)

        uname = request.session['username'] = username
        psw = request.session['password'] = password
        eml = request.session['signup_email'] = email
        mob = request.session['mobile'] = mobile
        otp_key = request.session['opt_gen'] = opt_gen

        context = {
            'uname': uname,
            'otp_key': otp_key,
        }
        return render(request, 'opt.html', context)
    data = {
        'form': form
    }

    return render(request, 'user_register.html', data)


def user_login(request):
    if request.session.get('email', None):
        return redirect('dashboard')

    form = LoginForm(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')

        u = Users.objects.filter(email=email, password=password)
        if u.exists():
            request.session['email'] = email

            return redirect('dashboard')


        else:
            messages.warning(request, 'Your Emailid or Password Not Correct ')
            print('data not match')
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def user_logout(request):
    if not request.session.get('email', None):
        return redirect('login')
    del request.session['email']
    return redirect('login')


def dashboard(request):
    if not request.session.get('email', None):
        return redirect('login')
    login_email = request.session.get('email')
    u = Users.objects.get(email=login_email)
    data = {
        'u': u
    }
    return render(request, 'dashboard.html', data)


def user_changepassword(request):
    if not request.session.get('email', None):
        return redirect('login')
    form = ChangePasswordForm(request.POST or None)
    if form.is_valid():
        old = form.cleaned_data.get('old')
        new = form.cleaned_data.get('new')
        repeat = form.cleaned_data.get('repeat')
        if new != repeat:
            messages.warning(request, 'Your Enter Password Not Match')
            return redirect('change_password')
        email = request.session.get('email')
        u = Users.objects.filter(password=old, email=email).update(password=new)
        if u:

            messages.warning(request, 'Your password Updated..')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Your Old Password Not Correct')

        print(old, new)

    content = {
        'form': form
    }
    return render(request, 'user_changepassword.html', content)


def user_resetpassword(request):
    form = ResetPasswordForm(request.POST or None)
    if 'otp_code' in request.POST:
        in_otp = request.POST.get('otp_code')

        ses_key = request.session.get('myotp')
        email = request.session.get('email')

        print(in_otp, type(in_otp), ses_key, type(ses_key))
        if int(in_otp) == int(ses_key):
            return redirect('new_password')

        else:
            return render(request, 'opt.html', {'mes': 'Opt Not Correct'})

    if form.is_valid():
        email = form.cleaned_data.get('email')
        otp = random.randrange(1111, 99999)
        request.session['myotp'] = otp
        request.session['email'] = email
        return render(request, 'opt.html', {'uname': email, 'otp_key': otp})

    content = {
        'form': form
    }
    return render(request, 'user_resetpassword.html', content)


def new_password(request):
    form = NewPasswordForm(request.POST or None)
    if form.is_valid():

        new = form.cleaned_data.get('new')
        repeat = form.cleaned_data.get('repeat')
        if new != repeat:
            messages.warning(request, 'Your Enter Password Not Match')
            return redirect('new_password')
        email = request.session.get('email')
        u = Users.objects.filter(email=email).update(password=new)
        if u:

            messages.warning(request, 'Your password Updated..')
            return redirect('login')
        else:
            messages.warning(request, 'Your Reapeat Password Not Match')

    content = {
        'form': form
    }
    return render(request, 'user_changepassword.html', content)


def user_profile(request):
    if not request.session.get('email'):
        return redirect('login')

    login_usr = request.session.get('email')
    usr = Users.objects.get(email=login_usr)
    p = UserProfile.objects.get(user=usr)

    content = {
        'login_usr': usr,
        'p': p
    }
    return render(request, 'profile.html', content)


def edit_profile(request):
    login_usr = request.session.get('email')
    usr = Users.objects.get(email=login_usr)
    pro = UserProfile.objects.get(user=usr)

    # form = ProfleForm(request.POST or None, request.FILES or None, instance=pro)
    # if form.is_valid():
    #     form.save()
    #     return redirect('profile')
    #
    # content = {
    #     'form': form
    # }
    # return render(request, 'edit_profile.html', content)