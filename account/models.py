from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UpdateBalanceOperationType:
    ADD = 1
    SUBTRACT = 2


class UserCustom(AbstractUser):
    balance = models.FloatField(verbose_name="Số dư", default=0)

    def update_balance(self, amount, operation=UpdateBalanceOperationType.ADD):
        if operation == UpdateBalanceOperationType.ADD:
            self.balance += amount
        elif operation == UpdateBalanceOperationType.SUBTRACT:
            self.balance -= amount
        self.save()

    def get_full_name(self) -> str:
        return self.last_name + " " + self.first_name
