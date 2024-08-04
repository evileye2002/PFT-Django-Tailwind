from django.urls import path
from . import views

urlpatterns = [
    path("sign-in", views.sign_in, name="htmx-sign-in"),
    path("sign-up", views.sign_up, name="htmx-sign-up"),
]

transaction_url_patterns = [
    path(
        "add-transaction",
        views.add_transaction,
        name="htmx-add-transaction",
    ),
    path(
        "transaction-deltail/<int:id>",
        views.transaction_deltail,
        name="htmx-transaction-deltail",
    ),
    path(
        "update-transaction/<int:id>",
        views.update_transaction,
        name="htmx-update-transaction",
    ),
    path(
        "delete-transaction/<int:id>",
        views.delete_transaction,
        name="htmx-delete-transaction",
    ),
    path(
        "category-option",
        views.category_option,
        name="htmx-category-option",
    ),
]

category_url_patterns = [
    path(
        "add-category",
        views.add_category,
        name="htmx-add-category",
    ),
    path(
        "category-deltail/<int:id>",
        views.category_deltail,
        name="htmx-category-deltail",
    ),
    path(
        "update-category/<int:id>",
        views.update_category,
        name="htmx-update-category",
    ),
    path(
        "delete-category/<int:id>",
        views.delete_category,
        name="htmx-delete-category",
    ),
]

urlpatterns += category_url_patterns
urlpatterns += transaction_url_patterns
