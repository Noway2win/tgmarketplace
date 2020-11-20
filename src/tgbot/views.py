from django.shortcuts import render
from .forms import ProfileForm


def index(request):
    form = ProfileForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()
    return render(request, "tgbot/index.html", locals())
