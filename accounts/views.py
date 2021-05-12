from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

# This class essentially instantiates a premade form
# and passes that to the specified template_name as 'form'
class Signup(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('dashboard')
    template_name = 'accounts/signup.html'

    # A 'generic.CreateView' method/function,
    # which lets us do the form validation ourselves
    def form_valid(self, form):
        view = super(Signup, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view
