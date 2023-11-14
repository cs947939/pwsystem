from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from urllib.request import Request
from .models import Device, ServerKeys, ChallengeCache
import base64
import os
import secrets
from pwmanager.models import Encryption, Data_ID
import cryptography
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import requests
from django.shortcuts import redirect

# Create your views here.
n = 14595161
x = 25612561
d = 54451625
def TrustedDeviceInit(request):
    if request.METHOD!="GET":
        devicekeypair = RSA.generate(2048)
        deviceprivate = devicekeypair.exportkey()
        response = HttpResponse("munchy")
        response.set_cookie('privatekey', deviceprivate)
        devicepublic = devicekeypair.publickey().export_key()
        response.set_cookie('public', devicepublic)
        name = request.POST.get('name')
        user = request.User.get()
        model = Device()
        model.Name = name
        model.Owner = user
        model.Pub_key = devicepublic
        return response
    else:
        return render(request, "postinit.html")

def CookieCheck(request):
    public = request.COOKIES.get('public')
    private = request.COOKIES.get('privatekey')
    return HttpResponse(public + private)

    