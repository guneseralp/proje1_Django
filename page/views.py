from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def home_view(request):
    # print("request::::",request)
    context={}
    return render(request,"page/home_page.html",context)

def about_us_view(request):
    page_title="Hakkimizda"
    hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam efficitur fringilla eros, vitae bibendum libero efficitur finibus. Suspendisse potenti. Nullam ullamcorper tortor ut sodales convallis. Phasellus sollicitudin lorem ac massa scelerisque, non molestie leo lobortis. Donec mattis malesuada accumsan. Vivamus lectus ante, tincidunt convallis vestibulum id, fermentum ut erat. Integer ac purus hendrerit, rutrum velit a, blandit nisl."
    contexet = {
        "page_title": page_title,
        "hero_content": hero_content,
    }
    return render(request,'page/about_us.html', context)

def contact_us_view(request):
    page_title="Iletişim"
    hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam efficitur fringilla eros, vitae bibendum libero efficitur finibus. Suspendisse potenti. Nullam ullamcorper tortor ut sodales convallis. Phasellus sollicitudin lorem ac massa scelerisque, non molestie leo lobortis. Donec mattis malesuada accumsan. Vivamus lectus ante, tincidunt convallis vestibulum id, fermentum ut erat. Integer ac purus hendrerit, rutrum velit a, blandit nisl."
    context=dict(
        page_title=page_title,
        hero_content = hero_content
    )
    return render(request,'page/contact_us.html', context)

def vision_view(request):
    page_title="Vizyonumuz"
    context=dict(
        page_title=page_title
    )
    return render(request,'page/vision.html', context)