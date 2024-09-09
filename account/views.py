from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect
from .forms import InscriptionForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm



def connexion(request):
    if request.user.is_authenticated:
        return redirect('articles:article_view')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Connexion réussie !')
                return redirect('articles:article_view')
            else:
                messages.error(request, 'Informations incorrectes.')
        else:
            messages.error(request, 'Veuillez les caracteres valides dans le formulaire')
    else:
        form = AuthenticationForm()

    return render(request, 'account/connexion.html', {'form': form})



def inscription(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = InscriptionForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request,user)
                messages.success(request,'votre compte a été cree avec succes ')
                return redirect('articles:article_view')
        else:
            form = InscriptionForm()
    else:
        return redirect('articles:article_view')
    return render(request=request,template_name='account/inscription.html',context={'form':form})

def deconnexion(request):
    logout(request)
    messages.success(request,'vous avez été deconnecter avec succes')
    return redirect('articles:article_view')



def recuperation(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            messages.error(request, 'Veuillez entrer un email valide')
            return render(request, 'account/password_forgot.html')
        
        user = User.objects.filter(email=email).first()
        
        if user:
            return redirect('confirme_password', email=email)
        else:
            messages.error(request, 'Aucun compte associé à cette adresse')
            return render(request, 'account/password_forgot.html')

    return render(request, 'account/password_forgot.html')

def confirme(request, email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        messages.error(request, 'Utilisateur non trouvé')
        return redirect('forgot')

    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Les mots de passe ne correspondent pas')
        elif len(password2) < 6:
            messages.error(request, 'Le mot de passe doit contenir au moins 6 caractères')
        elif not any(char.isdigit() for char in password2):
            messages.error(request, 'Le mot de passe doit contenir au moins un chiffre')
        elif not any(char.isalpha() for char in password2):
            messages.error(request, 'Le mot de passe doit contenir au moins une lettre')
        else:
            user.set_password(password2)
            user.save()
            messages.success(request, 'Votre mot de passe a été mis à jour avec succès')
            return redirect('login')
    
    return render(request, 'account/new_password.html', {'email': email})
