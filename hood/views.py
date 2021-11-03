from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def registration(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if confirm_password == password:
            if User.objects.filter(username=username):
                messages.info(request, 'A user with this Username already exists!')
                return redirect('registration')
            elif User.objects.filter(email=email):
                messages.info(request, 'The Email already exists')
                return redirect('registration')
            else:
                user = User.objects.create_user(firstname, lastname, username, email, password)
                user.save()

                return redirect('home')

        else:
            messages.info(request, 'Both passwords should match!')
            return redirect('registration')
    else:
        return render(request, 'auth/signup.html')

@login_required
def home(request):

    return render(request, 'index.html')
