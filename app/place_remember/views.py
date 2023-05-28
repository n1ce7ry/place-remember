from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount

def home(request):
    try:
        user_info = SocialAccount.objects.get(user=request.user)
        context = {
            "provider": user_info.provider,
            "user_info": user_info.extra_data,
        }
        return render(request=request, template_name="place_remember/index.html", context=context)
    except Exception:
        return render(request=request, template_name="place_remember/index.html")

