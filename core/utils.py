from datetime import datetime, date, timedelta
from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncDay, TruncWeek
import calendar
from .models import Transaction, TransactionType

VIETNAMESE_WEEKDAYS = {
    "Monday": "Thứ Hai",
    "Tuesday": "Thứ Ba",
    "Wednesday": "Thứ Tư",
    "Thursday": "Thứ Năm",
    "Friday": "Thứ Sáu",
    "Saturday": "Thứ Bảy",
    "Sunday": "Chủ Nhật",
    "Mon": "T2",
    "Tue": "T3",
    "Wed": "T4",
    "Thu": "T5",
    "Fri": "T6",
    "Sat": "T7",
    "Sun": "CN",
}
