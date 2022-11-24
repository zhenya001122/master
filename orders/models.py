from django.db import models

from profiles.models import Address
from users.models import User


STATUS_CHOICES = [
    ('оплачен', 'оплачен'),
    ('отправлен', 'отправлен'),
    ('доставлен', 'доставлен'),
    ('получен', 'получен'),
]


class Order(models.Model):
    user = models.ForeignKey(
        User, related_name="orders", on_delete=models.CASCADE
    )
    address = models.ForeignKey(Address, related_name="orders", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True, null=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
