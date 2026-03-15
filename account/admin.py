from django.contrib import admin
from .models import CustomUser

# 管理サイトへのモデルの追加
from django.contrib import admin

# 管理サイトにCustomUserモデルを追加
# 「http://127.0.0.1:8000/admin/」で管理できるように
class CustomUserAdmin(admin.ModelAdmin):
    # CustomUserモデルは13項目のうち、
    # 管理サイト（/admin）に表示するのは下記の2つ
    list_display = ('id', 'username')
    list_display_links = ('id', 'username')

# createsuperuserで作成した管理者も登録しておく
admin.site.register(CustomUser, CustomUserAdmin)