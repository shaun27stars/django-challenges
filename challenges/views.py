from django.http.response import Http404
from django.shortcuts import redirect, render
from django.http import Http404
from django.urls.base import reverse

challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Learn Django for at least 20 minutes every day!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Walk for at least 20 minutes every day!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Learn Django for at least 20 minutes every day!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}

# Create your views here.


def index(request):
    months = list(challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_by_number(request, month):
    months = list(challenges.keys())
    if month > len(months) or month < 1:
        raise Http404()
    month_name = months[month - 1]
    redirect_path = reverse("month-challenge", args=[month_name])
    return redirect(redirect_path)


def monthly_challenges(request, month):
    if month in challenges:
        challenge_text = challenges[month]
    else:
        raise Http404()

    return render(request, 'challenges/show.html', {
        "month": month,
        "challenge_text": challenge_text
    })
