from django.db import models
from users.models import User


class Blog(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blogs",
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f'{self.author}. {self.title} {self.text} {self.created_at}'
