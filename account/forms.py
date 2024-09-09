from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
    
class InscriptionForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'Indiquez votre Email',
        })
    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Indiquez le Prénom',
        }),
        label = "Nom"
    )

    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Indiquez le Nom de famille',
        })
       ,
       label = "Prénom"
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        #Stylisation des champs
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Indiquez le Nom d\'utilisateur',
                'autofocus': 'autofocus'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Indiquez le Mot de Passe',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirmez le Mot de Passe',
            }),
        }

        labels = {
            
            'email': 'Adresse Email',
            'username': 'Nom Utilisateur',
            'password1': 'Mot de passe',
            'password2': 'Confirmez le mot de passe',
        }

    # Validation de l'email de l'utilisateur
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déjà utilisé.")
        return email