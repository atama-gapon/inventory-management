from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, FormView
from inventory_register.models import Inventory

from django.urls import reverse_lazy
from .forms import ContactForm
from django.core.mail import EmailMessage

from django.db.models import Q


class HomeView(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    model = Inventory
    queryset = Inventory.objects.order_by('-updated_at')
    paginate_by = 8

    # 参考リンク
    # https://www.useful-python.com/django-search-in-page/#index_id0

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)

        # formで送信したクエリパラメータを取得
        query = self.request.GET

        if q := query.get('search_word'):

            # 商品名、商品番号、説明文、これらのデータをもとに検索を行う
            queryset = queryset.filter(Q(item_name__icontains=q)|Q(part_number__icontains=q)|Q(description__icontains=q))

        # セイウチ演算子で書かれたものを分解すると ↓

        # q = query.get('search_word')
        # if q:
        #     queryset = queryset.filter(item_name__icontains=q)

        return queryset.order_by('-updated_at')



# フォーム（問い合わせ等の入力画面）を活用するため、FormViewを継承
class ContactView(LoginRequiredMixin, FormView):
    # 使用するテンプレート（HTML）を指定
    template_name = 'contact.html'

    # ContactFormクラスを活用
    form_class = ContactForm

    # 問い合わせ送信"完了後"のURL（行き先）を指定
    success_url = reverse_lazy('inventory_browse:contact_success')

    # メール送信（問い合わせ送信）のメソッド
    def form_valid(self, form):

        # HTML（フォーム）から送られたデータを各変数に格納
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']

        ##### 送信準備 #####
        # メールのタイトルを指定
        subject = 'お問い合わせ: {}'.format(title)
        # メールの本文を設定
        message = '送信者名:{0}\nメールアドレス:{1}\nタイトル:{2}\nメッセージ:{3}\n'.format(name, email, title, message)

        # 送信元のメールアドレスを設定
        from_email = 'example@example.com'
        # 宛先のメールアドレスを設定
        to_list = ['example@example.com']

        # タイトル、本文、送信元、宛先をまとめる
        # EmailMessageクラスをインスタンス化してmessageオブジェクトを生成
        message = EmailMessage(subject=subject,
                                body=message,
                                from_email=from_email,
                                to=to_list)

        # メール送信
        # messageオブジェクトのsendメソッドを実行（メール送信）
        message.send()

        # 戻り値
        return super().form_valid(form)

class ContactSuccessView(LoginRequiredMixin, TemplateView):
    template_name="contact_success.html"