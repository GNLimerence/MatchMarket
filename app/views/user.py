from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ..forms.user import SignupForm

def login_user (request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("ErrorLogin"))
            return redirect('login')
    else:
        context = {
            "title" : "ログイン",
        }
        return render(request, "user/login.html", context)

def logout_user (request):
    logout(request)
    messages.success(request, ("Log out success"))
    return redirect('login')

def register_user (request):
    if request.method == 'POST':
        print(request.POST)
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='index')

    else:
        form = SignupForm()
    
    param = {
        'form': form,
        'title': 'ユーザー登録',
    }

    return render(request, 'user/register.html', param)
