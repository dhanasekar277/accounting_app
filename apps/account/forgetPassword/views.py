from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def ForgetPassword(request):

    if request.method == 'POST':

        post_ = request.POST
        post_ = list(post_.keys())

        if post_[1] == 'email-check':

            email = request.POST['email-check']
            check_user = User.objects.filter(email=email)
            if check_user:
                context = {
                    'user_info': check_user
                }
                return render(request, 'account/forget-password.html', context=context)
            else:
                messages.error(request, 'Invalid Email Address. !!!')


        if post_[1] == 'password':

            password = request.POST['password']
            confir_password = request.POST['confirm-password']

            email = request.POST['email']
            check_user = User.objects.filter(email=email)

            if password ==  confir_password:
                u = User.objects.get(email=email)
                u.set_password(password)
                u.save()
                context = {
                    'password_updated': 'Password Updated Successfully. !!!!'
                }
                return render(request, 'account/forget-password.html', context=context)
            else:
                context = {
                    'user_info': check_user
                }
                messages.error(request, 'Password Does\'t Match. !!!')
                return render(request, 'account/forget-password.html', context=context)

    return render(request, 'account/forget-password.html')


