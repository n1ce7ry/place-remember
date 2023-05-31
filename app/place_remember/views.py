from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount
from .models import Memory
from .forms import MemoryForm


def home(request):
    try:
        user_info = SocialAccount.objects.get(user=request.user)
        memory_data = Memory.objects.filter(user_id__user=request.user)
        context = {
            "provider": user_info.provider,
            "user_info": user_info.extra_data,
            'memory_data': memory_data,
        }
        return render(request=request, template_name="place_remember/index.html", context=context)
    except TypeError:
        return render(request=request, template_name="place_remember/index.html")


def add_memory(request):
    try:
        user_info = SocialAccount.objects.get(user=request.user)

        if request.method == 'POST':
            form = MemoryForm(request.POST)
            if form.is_valid():
                memory = form.save(commit=False)
                memory.user_id = SocialAccount.objects.get(user=request.user)
                memory.save()
                return redirect('home')
            else:
                return render(request, 'place_remember/add_memory.html',
                              {'form': form, 'provider': user_info.provider,
                               'user_info': user_info.extra_data, 'error': 'Выберите место на карте'})
        else:
            form = MemoryForm()
            return render(request, 'place_remember/add_memory.html',
                          {'form': form, 'provider': user_info.provider,
                           'user_info': user_info.extra_data})
    except TypeError:
        return redirect('home')
