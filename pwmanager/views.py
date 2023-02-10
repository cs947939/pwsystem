from django.shortcuts import render
from .models import Password, Encryption
from .forms import PasswordForm, KeyForm
from datetime import date
from django.shortcuts import redirect
from django.http import HttpResponse
from cryptography.fernet import Fernet

def setup(request):
    if request.method == "POST":
        ekey = Encryption()
        
        ekey.Owner = request.user
        ekey.save() 

        return redirect('/')

        


def add(request):
    
    if request.method == "POST":
        
        ekey = Encryption.objects.get(Owner=request.user)
        token = ekey.Key
        s = Password()
        ks = Fernet(token)
       
        user = request.POST['username']
        pw = request.POST['Password']
        pw2 = bytes(pw, 'UTF-8')
        newPassword = ks.encrypt(pw2)
        newPassword2 = str(newPassword,'UTF-8')
        pw = newPassword2
        TOTP = request.POST['TOTP']
        T2 = bytes(TOTP, 'UTF-8')
        newTOTP = ks.encrypt(T2)
        newTOTP2 = str(newTOTP, 'UTF-8')
        TOTP = newTOTP2
        Atachment = request.POST['File']
        Date = request.POST['date']
        Owner = request.user
        s.Username = user
        s.Password = newPassword2
        s.TOTP = newTOTP2
        s.Atachment = Atachment
        s.Date_Created = Date
        s.Owner = Owner
        s.save()
        
           
        return redirect('/')

# Create your views here.