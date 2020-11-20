from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
# Account create view -> use custom form, not generic form

def register(request):
    if request.method == "POST":
        # post sent for registration
        # recreate form from post content
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else:
        # get for registration page
        user_form = RegisterForm()
        return render(request, 'registration/register.html', {'form':user_form} )
