from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.monthly_challenges_by_number),
    # defaults to string if omitted
    path("<str:month>", views.monthly_challenges, name="month-challenge"),
    path("", views.index, name="index")
]
