from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class TransactionType(models.IntegerChoices):
    INCOME = 1, "Thu nhập"
    EXPENSE = 2, "Chi tiêu"


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField(choices=TransactionType.choices)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500, null=True, blank=True)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="tCategory"
    )
    name = models.CharField(max_length=150)
    type = models.IntegerField(choices=TransactionType.choices)
    amount = models.FloatField()
    date = models.DateField()
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
