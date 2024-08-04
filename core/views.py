from django.shortcuts import render, resolve_url
from django.contrib.auth.decorators import login_required
from .models import Transaction, Category, TransactionType
from .charts import ColumnChart, ChartType, DonutChart


# Create your views here.
@login_required(login_url="sign-in")
def home(request):
    start_str = request.GET.get("start")
    end_str = request.GET.get("end")
    c_type = request.GET.get("type", "week")

    try:
        cc_income, cc_expense = ColumnChart(
            request.user,
            c_type,
            start_str,
            end_str,
        ).get_data_str()
    except Exception as ex:
        cc_income = None
        cc_expense = None

    dn_colors = []
    dn_income, dn_expense = DonutChart(
        request.user,
        c_type,
        start_str,
        end_str,
    ).get_data_str()

    ctx = {
        "report_type": c_type,
        "start_string": start_str,
        "end_string": end_str,
        "cc_income": cc_income,
        "cc_expense": cc_expense,
        "dn_income": dn_income,
        "dn_expense": dn_expense,
        "dn_colors": dn_colors,
    }

    return render(request, "core/index.html", ctx)


@login_required(login_url="sign-in")
def transaction(request):
    transactions = Transaction.objects.filter(user=request.user)
    categories = Category.objects.filter(
        user=request.user, type=TransactionType.EXPENSE
    )
    ctx = {
        "transactions": transactions,
        "categories": categories,
    }

    return render(request, "core/transaction.html", ctx)


@login_required(login_url="sign-in")
def category(request):
    categories = Category.objects.filter(user=request.user)
    ctx = {"categories": categories}
    return render(request, "core/category.html", ctx)
