from django.db import models
# アカウントアプリ（別のアプリ）のモデルを使用 ⇒ インポート
from account.models import CustomUser

from django.urls import reverse

# class Category(models.Model):
#     ''' カテゴリ管理のテーブル '''
#     title = models.CharField(
#                             verbose_name='カテゴリ', # フィールド名
#                             max_length=20 # 文字の最大数
#                             )

#     def __str__(self):
#         return self.title

class Inventory(models.Model):
    ''' 在庫全般を管理するテーブル '''
    # ユーザー：CustomUserモデルと紐付け
    # カテゴリ：Categoryモデルと紐付け
    # タイトル：通常通り
    # コメント：通常通り
    # イメージ1：必須
    # イメージ2：任意

    # 品番
    # 商品名
    # 単価
    # 在庫数
    # 説明文
    # 商品画像
    # 作られた日時
    # 最後に更新された日時

    # コメント（編集画面で更新を行ったときに入力する）


    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', 
                            # ユーザーを削除するとき：CASCADE（繋ぐ） ⇒ 投稿データをすべて削除
                            # CASCADE：繋がっているものはすべて削除する
                            on_delete=models.CASCADE)

    # category = models.ForeignKey(Category, verbose_name='カテゴリ', 
    #                             # カテゴリを削除するとき：PROTECT（守る・保護する） ⇒ 
    #                             # 投稿側にある場合は、カテゴリ側も削除できない
    #                             # PROTECT：繋がっているものがあれば削除できない
    #                             on_delete=models.PROTECT)

    part_number = models.CharField(verbose_name='商品番号', max_length=30, unique=True)

    # 商品名のmax_lengthは？CharFieldで本当にいい？
    item_name = models.CharField(verbose_name='商品名', max_length=50)

    unit_price = models.IntegerField(verbose_name='単価')

    # なにも入力しないのも許可して、デフォルト値を「０」に設定もあり？
    inventory_quantity = models.IntegerField(verbose_name='在庫数')

    description = models.TextField(verbose_name='説明文')

    # image1 = models.ImageField(verbose_name='イメージ1', upload_to='item_images', blank=True, null=True)

    image1 = models.ImageField(verbose_name='イメージ1', upload_to='item_images')

    ''' 参考
    https://akiyoko.hatenablog.jp/entry/2020/05/22/081840
    '''
    created_at = models.DateTimeField('登録日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.item_name

    '''
    https://note.com/marketscience/n/n58b3b2cce5b0
    '''
    def get_absolute_url(self):
        return reverse("inventory_register:detail", args=[self.id])