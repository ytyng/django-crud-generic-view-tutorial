from django.db import models


class Memo(models.Model):
    subject = models.CharField(
        verbose_name='件名',
        max_length=100,
        default='',
        blank=True
    )

    body = models.TextField(
        verbose_name='本文',
        default='',
        blank=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )
