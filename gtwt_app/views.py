from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages

# Home view
def home(request):
    return render(request, 'home.html')

from django import forms
from django.contrib.auth.models import User

# Custom user registration form
class CustomUserCreationForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30, 
        required=True, 
        label="First Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30, 
        required=True, 
        label="Last Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    username = forms.CharField(
        max_length=150, 
        required=True, 
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), 
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}), 
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# Register View
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created. Please log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Auth/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'Auth/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Password Reset Views
def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                use_https=request.is_secure(),
                from_email="gtmovies2340@gmail.com",  # Replace with your email or environment variable
                subject_template_name='registration/password_reset_subject.txt',
                email_template_name='registration/password_reset_email.html',
            )
            messages.success(request, 'Password reset link sent. Please check your email.')
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'Auth/password_reset.html', {'form': form})

def password_reset_done_view(request):
    return render(request, 'Auth/password_reset_done.html')

def password_reset_confirm_view(request, uidb64, token):
    # Django handles password reset confirm view automatically
    return auth_views.PasswordResetConfirmView.as_view(
        template_name='Auth/password_reset_confirm.html',
        post_reset_redirect='password_reset_complete'
    )(request, uidb64=uidb64, token=token)

def password_reset_complete_view(request):
    return render(request, 'Auth/password_reset_complete.html')