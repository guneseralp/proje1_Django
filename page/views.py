from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # print("request::::",request)
    return render(request,"pade/home_page.html",{})