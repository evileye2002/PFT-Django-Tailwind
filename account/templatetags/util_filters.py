from django import template
from django.shortcuts import resolve_url
from core.models import TransactionType

register = template.Library()


@register.filter
def get_all_quert_parameters(request, url):
    query_params = request.GET.dict()
    resolved_url = resolve_url(url)

    if query_params:
        return (
            resolved_url
            + "?"
            + "&".join(f"{key}={value}" for key, value in query_params.items())
        )
    return resolved_url


@register.filter
def check_transaction_type(transaction, args):
    con1, con2 = args.split(",")
    if transaction.type == TransactionType.INCOME:
        return con1
    elif transaction.type == TransactionType.EXPENSE:
        return con2
    return ""


@register.filter
def int_comma(value):
    try:
        value_str = "{:,}".format(int(value))
        return value_str
    except (ValueError, TypeError):
        return value
