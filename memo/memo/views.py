from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import \
    ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Memo
from .forms import MemoForm


class MemoListView(ListView):
    """
    メモを一覧表示
    """
    model = Memo


class MemoDetailView(DetailView):
    """
    1つのメモを詳細表示
    """
    model = Memo


class MemoCreateView(CreateView):
    """
    メモ 新規作成
    """
    model = Memo
    form_class = MemoForm
    success_url = reverse_lazy('memo_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を作成しました'.format(form.instance))
        return result


class MemoUpdateView(UpdateView):
    """
    メモ 更新
    """
    model = Memo
    form_class = MemoForm

    success_url = reverse_lazy('memo_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を更新しました'.format(form.instance))
        return result


class MemoDeleteView(DeleteView):
    """
    メモ 削除
    """
    model = Memo
    form_class = MemoForm

    success_url = reverse_lazy('memo_list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, '「{}」を削除しました'.format(self.object))
        return result
