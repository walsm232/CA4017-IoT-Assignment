from django.http import HttpResponse
from django.shortcuts import render, redirect
import subprocess

from django.core import management

def Homepage(request):
    return render(request, 'main/index.html')

def Connect_Device(request):
    if request.POST:
        handle = subprocess.Popen([
        'powershell.exe',
        'C:/Users/Michael/Desktop/CA4017-IoT-Assignment/IoTWebApp/IoTWebApp/start.ps1',
        ], stdout=subprocess.PIPE)
        output = handle.stdout.read().decode('utf-8')
    return HttpResponse(output)