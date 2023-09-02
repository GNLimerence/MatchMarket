from django.shortcuts import render

def index(request):
    context = {
        "title": "MatchMarket",
    }
    return render(request, "index.html", context)