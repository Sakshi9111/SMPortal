from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			#return redirect('iissite')
			return redirect('home')

		else:
			#messages.success(request, ("Please login with correct credentials!"))	
			return redirect('login')	


	else:
		return render(request, 'authenticate/login.html', {})

def logout_user(request):
	logout(request)
	#messages.success(request, ("You are logged out!"))
	return redirect('login')	
