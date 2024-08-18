from django.urls import path
from . import views

urlpatterns = [
    path("sign-in", views.sign_in, name="htmx-sign-in"),
    path("sign-up", views.sign_up, name="htmx-sign-up"),
    path("update-user-info", views.update_user_info, name="htmx-update-user-info"),
    path("change-password", views.change_password, name="htmx-change-password"),
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
        "filter-transaction",
        views.filter_transaction,
        name="htmx-filter-transaction",
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
    path(
        "filter-category",
        views.filter_category,
        name="htmx-filter-category",
    ),
]

goal_url_patterns = [
    path(
        "add-goal",
        views.add_goal,
        name="htmx-add-goal",
    ),
    path(
        "goal-deltail/<int:id>",
        views.goal_deltail,
        name="htmx-goal-detail",
    ),
    path(
        "update-goal/<int:id>",
        views.update_goal,
        name="htmx-update-goal",
    ),
    path(
        "delete-goal/<int:id>",
        views.delete_goal,
        name="htmx-delete-goal",
    ),
]

urlpatterns += category_url_patterns
urlpatterns += transaction_url_patterns
urlpatterns += goal_url_patterns
