from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UsersLoginForm

def login_view(request):
	form = UsersLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username = username, password = password)
		login(request, user)
		return redirect("/")
	return render(request, "a_a/form.html", {
		"form" : form,
		"title" : "Login",
	})