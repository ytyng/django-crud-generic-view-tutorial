from django import forms

from .models import Memo


class MemoForm(forms.ModelForm):
    """
    Memo モデルの作成、更新に使われる Django フォーム。
    ModelForm を継承して作れば、HTMLで表示したいフィールドを
    指定するだけで HTML フォームを作ってくれる。
    """

    class Meta:
        model = Memo
        fields = ['subject', 'body']
