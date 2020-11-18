from django.shortcuts import render


def index(request):
    return render(
        request,
        "tgbot/index.html",
        {
            "page_place": "Main Page",
            "system": "Path",
        },
    )
