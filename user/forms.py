from django import forms 


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label="UserName")
    email = forms.EmailField(max_length=70,label="Email",widget=forms.EmailInput)
    password = forms.CharField(max_length=30,label="Password",widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=30,label="Password Confirm",widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        email = self.cleaned_data.get("email")

        if username and password and password != password_confirm:
            raise forms.ValidationError("Parola eşleşmiyor")
        
        values = {
            "username": username,
            "password": password,
            "email": email
        }
        return values
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label="UserName")
    password = forms.CharField(max_length=30,label="Password",widget=forms.PasswordInput)
