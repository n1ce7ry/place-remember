from django.shortcuts import render

def home(request):
    return render(request=request, template_name="place_remember/index.html")

