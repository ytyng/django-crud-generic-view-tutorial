from django.db import models


class Memo(models.Model):
    """
    メモモデル。実質、件名と本文のみ。
    """
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

    # created: auto_now_add を指定すると、作成日時を自動保存する
    created = models.DateTimeField(
        auto_now_add=True
    )

    # updated: auto_now を指定すると、更新日時を自動保存する
    updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.subject
