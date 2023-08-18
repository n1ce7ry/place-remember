from django.shortcuts import render, redirect
from .services.services import get_user_memories, get_user_social_data
from .forms import MemoryForm


def home(request):
    if request.user.is_authenticated:
        user_info = get_user_social_data(request.user)
        memory_data = get_user_memories(request.user)
        context = {
            "provider": user_info.provider,
            "user_info": user_info.extra_data,
            "memory_data": memory_data,
        }
        return render(
            request=request,
            template_name="place_remember/index.html",
            context=context
        )

    return render(
        request=request,
        template_name="place_remember/index.html"
    )


def add_memory(request):
    user_info = get_user_social_data(request.user)

    if request.method == "POST":
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.user_id = request.user
            memory.save()
            return redirect("home")
        else:
            return render(
                request,
                "place_remember/add_memory.html",
                {
                    "form": form,
                    "provider": user_info.provider,
                    "user_info": user_info.extra_data,
                    "error": "Выберите место на карте",
                },
            )
    else:
        form = MemoryForm()
        return render(
            request,
            "place_remember/add_memory.html",
            {
                "form": form,
                "provider": user_info.provider,
                "user_info": user_info.extra_data,
            },
        )
