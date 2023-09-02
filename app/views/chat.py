from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from ..models import Chat, User, Matching


def MatchingPage (request):
    match = Matching.objects.all()
    return render(request,"chat/chathomepage.html",{"match":match})
def chat(request, matching_id):
    user = request.user
    get_match = Matching.objects.get(id=matching_id)
    if request.method == 'POST':
        message = request.POST['message']
        print(message)
        new_message = Chat(matching_id=get_match, sender=user, message=message)
        new_message.save()

    get_messages = Chat.objects.filter(matching_id=get_match)

    context = {
        "messages": get_messages,
        "user": user,
        "matching_id": matching_id,
    }
    return render(request, 'chat/chat.html', context)

