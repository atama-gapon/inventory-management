# アカウント管理を行うCustomUsesrクラス（モデル）を作成する

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # 追加したいアカウントに持たせたい情報があれば記述
    pass


    # nickname = models.CharField(max_length=100)
    # height = models.FloatField()
    # weight = models.FloatField()

    # ＃＃＃＃上記のものを使用する場合、これが必要かも？
    # REQUIRED_FILEDS を設定することで、createsuperuser 
    # 実行時に username・email・nickname・height・weight・password 
    # の入力受付が行われるようになり、上手くユーザーを作成することができるようになります。

    # 「    # usernameとpasswordの指定は不要
    # REQUIRED_FIELDS = ["email", "nickname", "height", "weight"]」

    # emailの入力を必須に？
    # email = models.EmailField(blank=False)

    # 不要なフィールドを削除？
    # date_joined = None
'''
https://daeudaeu.com/django-abstractuser/#i
'''