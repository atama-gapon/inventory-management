from django.views.generic import TemplateView, CreateView, FormView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    # 登録が成功した場合、出来ればログインを勝手にしてホーム画面にいきたい
    success_url = reverse_lazy("account:register_success")

    # モデル（データベース）に保存する処理など
    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)

class RegisterSuccessView(TemplateView):
    template_name = 'register_success.html'