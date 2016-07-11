from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Counter


def index(request):
    return render(request, "index2.html", {
    })

@login_required
def counter(request):
    counter, created = Counter.objects.get_or_create(user=request.user)

    # Render that in the index template
    return render(request, "counter.html", {
        "counter": counter.count
    })
