from django import forms

# HTMLと連携し、フォーム（問い合わせ）機能を手助け
class ContactForm(forms.Form):

    # クラス変数を定義（変数定義）
    # 「お名前」は、CharField（文字列）
    name = forms.CharField(label='お名前')
    # 「メールアドレス」は、EmailField（@のメール形式）
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)