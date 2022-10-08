from django.db import models



class Blog(models.Model):
    author = models.ForeignKey(
        'users.User',
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
