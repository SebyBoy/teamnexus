from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Message


def get_user():
    return User.objects.first()


def inbox(request):
    user = get_user()
    messages = Message.objects.filter(receiver=user, is_draft=False)
    return render(request, "messaging/inbox.html", {"messages": messages})

def sent_messages(request):
    user = get_user()
    messages = Message.objects.filter(sender=user, is_draft=False)
    return render(request, "messaging/sent.html", {"messages": messages})

def drafts(request):
    user = get_user()
    messages = Message.objects.filter(sender=user, is_draft=True)
    return render(request, "messaging/drafts.html", {"messages": messages})

def send_message(request):
    user = get_user()

    if request.method == "POST":
        content = request.POST.get("content")
        action = request.POST.get("action")

        if content:
            if action == "draft":
                Message.objects.create(
                    sender=user,
                    receiver=user,
                    content=content,
                    is_draft=True
                )
            else:
                Message.objects.create(
                    sender=user,
                    receiver=user,
                    content=content,
                    is_draft=False
                )

            return redirect("inbox")

    return render(request, "messaging/send_message.html")


    return render(request, "messaging/send_message.html")


def message_detail(request, id):
    message = Message.objects.get(id=id)
    return render(request, "messaging/detail.html", {"message": message})


def vote_view(request):
    return render(request, "messaging/vote.html")


def summary_view(request):
    user = get_user()

    sent_count = Message.objects.filter(sender=user, is_draft=False).count()
    received_count = Message.objects.filter(receiver=user, is_draft=False).count()

    return render(request, "messaging/summary.html", {
        "sent_count": sent_count,
        "received_count": received_count
    })