from django.contrib import messages
from django.urls import reverse
from django.views.generic import \
    ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Memo
from .forms import MemoForm
from .tenancy import dbname, ensure_connect

class MemoListView(ListView):
    """
    メモを一覧表示
    テンプレートは、何も指定しないと モデル名_list.html が使われる
    ListView は、ページネーションもやってくれる
    """
    model = Memo
    paginate_by = 10  # 1ページに表示する件数

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dbnum'] = self.kwargs['dbnum']
        return context

    def get_queryset(self):
        dbnum = self.kwargs['dbnum']
        ensure_connect(dbnum)
        return Memo.objects.using(dbname(dbnum)).all()


class MemoDetailView(DetailView):
    """
    1つのメモを詳細表示
    テンプレートは、何も指定しないと モデル名_detail.html が使われる
    """
    model = Memo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dbnum'] = self.kwargs['dbnum']
        return context

    def get_queryset(self):
        dbnum = self.kwargs['dbnum']
        ensure_connect(dbnum)
        return Memo.objects.using(dbname(dbnum)).all()


class MemoCreateView(CreateView):
    """
    メモ 新規作成
    完了ページを作成し、success_url で指定して表示してもいいが、
    django.contrib.messages の機能で、メッセージを保存して
    リストビューなんかに戻した時に表示するのも簡潔で良い。
    """
    model = Memo
    form_class = MemoForm

    def get_success_url(self):
        return reverse('memo_list', kwargs={'dbnum': self.kwargs['dbnum']})

    def form_valid(self, form):
        # form.instance にはsaveしていないモデルのインスタンスが入っている
        form.instance.save(using=dbname(self.kwargs['dbnum']))

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

    def get_success_url(self):
        return reverse('memo_list', kwargs={'dbnum': self.kwargs['dbnum']})

    def get_queryset(self):
        dbnum = self.kwargs['dbnum']
        ensure_connect(dbnum)
        return Memo.objects.using(dbname(dbnum)).all()

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を更新しました'.format(form.instance))
        return result


class MemoDeleteView(DeleteView):
    """
    メモ 削除
    デフォルトでは、get でリクエストすると確認ページ、
    post でリクエストすると削除を実行する、という動作。
    実際は、レコードを削除するのではなく有効フラグを消す(いわゆる論理削除)
    のケースが多いと思うので、そんな時はdeleteをオーバーライドしてその中で処理を書く。
    """
    model = Memo
    form_class = MemoForm

    def get_success_url(self):
        return reverse('memo_list', kwargs={'dbnum': self.kwargs['dbnum']})

    def get_queryset(self):
        return Memo.objects.using(dbname(self.kwargs['dbnum'])).all()

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, '「{}」を削除しました'.format(self.object))
        return result
