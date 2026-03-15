# フォームで使用する UserCreationForm をインポート
from django.contrib.auth.forms import UserCreationForm
# 連携するモデル（DB）の CustomUser をインポート
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # 連携するもの
    class Meta:
        # 使用するフォームのフィールド
        model = CustomUser
        # 入力を要求するフィールドを絞る、もしかしたら他にも必要なものがあるかも？
        # ユーザー名、メール、パスワード１、パスワード２（確認用）
        fields = ('username', 'email', 'password1', 'password2')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['password1'].widget.attrs['class'] = "form-control"
    #     self.fields['password1'].label = 'ユーザ名'

    #     self.fields['email'].widget.attrs['class'] = "form-control"
    #     self.fields['email'].widget.attrs['placeholder'] = "メールアドレス"
    #     self.fields['email'].widget.attrs['autocomplete'] = "email"
    #     self.fields['email'].widget.attrs['autocapitalize'] = "none"
    #     self.fields['email'].label = "メールアドレス"

    #     self.fields['email'].widget.attrs['id'] = "id_login"