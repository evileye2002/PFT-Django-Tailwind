from django.shortcuts import render, redirect
from django.contrib.auth import logout
from core.models import Transaction, Category
from .forms import UpdateUserInfoForm


def sign_in(request):
    if request.user.is_authenticated:
        return redirect("home")

    return render(request, "account/authentication.html")


def sign_up(request):
    return render(request, "account/authentication.html")


def sign_out(request):
    logout(request)
    return redirect("sign-in")


def profile(request):
    transaction_count = Transaction.objects.filter(user=request.user).count()
    category_count = Category.objects.filter(user=request.user).count()

    ctx = {
        "transaction_count": transaction_count,
        "category_count": category_count,
        "form": UpdateUserInfoForm(instance=request.user),
    }

    return render(request, "account/profile.html", ctx)
