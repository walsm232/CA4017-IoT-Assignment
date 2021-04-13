from django.http import HttpResponse
from django.shortcuts import render, redirect

def Homepage(request):
    return render(request, 'main/homepage.html')