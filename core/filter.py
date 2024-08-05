import django_filters
from .models import Transaction, TransactionType, Category


class TransactionFilter(django_filters.FilterSet):
    t_name = django_filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )
    t_type = django_filters.ChoiceFilter(
        choices=TransactionType.choices,
        field_name="type",
        lookup_expr="exact",
    )
    date = django_filters.DateFromToRangeFilter()

    category = django_filters.ModelMultipleChoiceFilter(queryset=None)

    class Meta:
        model = Transaction
        fields = ["t_name", "t_type", "date", "category"]

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super().__init__(data, queryset, request=request, prefix=prefix)

        self.form.fields["date"].fields[0].input_formats = ["%d-%m-%Y"]
        self.form.fields["date"].fields[-1].input_formats = ["%d-%m-%Y"]
        self.form.fields["category"].queryset = Category.objects.filter(
            user=request.user
        )
