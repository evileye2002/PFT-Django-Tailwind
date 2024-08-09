from django import template
from django.shortcuts import resolve_url

register = template.Library()

NAVBAR_LINKS = [
    {"href": resolve_url("home"), "title": "Trang chủ"},
    {"href": resolve_url("transaction"), "title": "Giao dịch"},
    {"href": resolve_url("category"), "title": "Hạng mục"},
    {"href": resolve_url("goal"), "title": "Mục tiêu"},
]

METADATA = {
    "webname": "ExMoney",
    "description": "",
}


@register.simple_tag
def get_navbar_links():
    return NAVBAR_LINKS


@register.simple_tag
def test_tag():
    return "Hello, world!"
