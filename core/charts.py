from datetime import datetime, date, timedelta
from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncDay, TruncWeek
import calendar

from .models import Transaction, TransactionType
from .utils import VIETNAMESE_WEEKDAYS


class ChartType:
    TODAY = "today"
    THIS_WEEK = "week"
    THIS_MONTH = "month"
    THIS_YEAR = "year"
    DAY_RANGE = "day-range"
    YEAR_RANGE = "year-range"


class BaseChart:
    def __init__(self, user, type: str, start_str: str, end_str: str):
        self.user = user
        self.type = type
        self.start_str = start_str
        self.end_str = end_str
        self.range = self.get_range()
        self.income_filter, self.expense_filter = self.get_filter()

    def get_range(self):
        if self.type == ChartType.THIS_YEAR:
            return (1, 12)

        if self.type == ChartType.THIS_MONTH:
            today = date.today()
            start = date(today.year, today.month, 1)
            last_day = calendar.monthrange(today.year, today.month)[1]
            end = date(today.year, today.month, last_day)
            return (start, end)

        if self.type == ChartType.THIS_WEEK:
            today = date.today()
            start_of_week = today - timedelta(days=today.weekday())
            end_of_week = start_of_week + timedelta(days=6)
            return (start_of_week, end_of_week)

        if self.type == ChartType.TODAY:
            today = date.today()
            return (today, None)

        if self.type == ChartType.DAY_RANGE:
            start = date.strptime(self.start_str, "%d-%m-%Y")
            end = date.strptime(self.end_str, "%d-%m-%Y")
            return (start, end)

        return (None, None)

    def get_filter(self):
        if self.type == ChartType.THIS_YEAR:
            incomes = Transaction.objects.filter(
                user=self.user,
                type=TransactionType.INCOME,
                date__year=date.today().year,
            )
            expenses = Transaction.objects.filter(
                user=self.user,
                type=TransactionType.EXPENSE,
                date__year=date.today().year,
            )

            return (incomes, expenses)

        if (
            self.type == ChartType.THIS_MONTH
            or self.type == ChartType.THIS_WEEK
            or self.type == ChartType.TODAY
            or self.type == ChartType.DAY_RANGE
        ):
            incomes = Transaction.objects.filter(
                user=self.user,
                type=TransactionType.INCOME,
                date__range=self.range,
            )
            expenses = Transaction.objects.filter(
                user=self.user,
                type=TransactionType.EXPENSE,
                date__range=self.range,
            )
            return (incomes, expenses)

        return (None, None)


class ColumnChart(BaseChart):
    def __init__(self, user, type: str, start_str: str, end_str: str):
        super().__init__(user, type, start_str, end_str)
        self.income_dict, self.expense_dict = self.get_data_dict()

    def get_data_dict(self):
        if self.type == ChartType.THIS_YEAR:
            incomes = (
                self.income_filter.annotate(month=TruncMonth("date"))
                .values("month")
                .annotate(total_amount=Sum("amount"))
                .order_by("date")
            )
            expenses = (
                self.expense_filter.annotate(month=TruncMonth("date"))
                .values("month")
                .annotate(total_amount=Sum("amount"))
                .order_by("date")
            )
            income_dict = {
                entry["month"].month: entry["total_amount"] for entry in incomes
            }
            expense_dict = {
                entry["month"].month: entry["total_amount"] for entry in expenses
            }

            return (income_dict, expense_dict)

        if (
            self.type == ChartType.THIS_MONTH
            or self.type == ChartType.THIS_WEEK
            or self.type == ChartType.TODAY
            or self.type == ChartType.DAY_RANGE
        ):
            return self.get_data_dict_by_day()

        return (None, None)

    def get_data_dict_by_day(self):
        incomes = (
            self.income_filter.annotate(day=TruncDay("date"))
            .values("day")
            .annotate(total_amount=Sum("amount"))
            .order_by("day")
        )
        expenses = (
            self.expense_filter.annotate(day=TruncDay("date"))
            .values("day")
            .annotate(total_amount=Sum("amount"))
            .order_by("day")
        )
        income_dict = {entry["day"]: entry["total_amount"] for entry in incomes}
        expense_dict = {entry["day"]: entry["total_amount"] for entry in expenses}

        return (income_dict, expense_dict)

    def get_data_str(self):
        start, end = self.range
        income_data_str = []
        expense_data_str = []

        if self.type == ChartType.THIS_WEEK or self.type == ChartType.THIS_MONTH:
            i = start
            while i <= end:
                y_income = self.income_dict.get(i, 0)
                y_expense = self.expense_dict.get(i, 0)

                if self.type == ChartType.THIS_WEEK:
                    x = VIETNAMESE_WEEKDAYS[i.strftime("%a")]
                else:
                    x = i.strftime("%d")

                income_data_str.append({"x": f"{x}", "y": y_income})
                expense_data_str.append({"x": f"{x}", "y": y_expense})
                i += timedelta(days=1)

            return (income_data_str, expense_data_str)

        if self.type == ChartType.THIS_YEAR:
            for i in range(start, end + 1):
                y_income = self.income_dict.get(i, 0)
                y_expense = self.expense_dict.get(i, 0)
                income_data_str.append({"x": f"Th{i:02d}", "y": y_income})
                expense_data_str.append({"x": f"Th{i:02d}", "y": y_expense})

            return (income_data_str, expense_data_str)


class DonutChart(BaseChart):
    def get_data_str(self):
        income = self.income_filter.values("category__name").annotate(
            total_amount=Sum("amount")
        )
        income_labels = [category["category__name"] for category in income]
        income_values = [int(category["total_amount"]) for category in income]

        expense = self.expense_filter.values("category__name").annotate(
            total_amount=Sum("amount")
        )
        expense_labels = [category["category__name"] for category in expense]
        expense_values = [int(category["total_amount"]) for category in expense]

        income_data = {"labels": income_labels, "values": income_values}
        expense_data = {"labels": expense_labels, "values": expense_values}

        return (income_data, expense_data)
