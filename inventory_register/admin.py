from django.contrib import admin
from .models import Inventory

# 管理ページで表示するフィールドを定義するため（CategoryAdmin・PhotoPostAdmin）
# class CategoryAdmin(admin.ModelAdmin):
#     # 表示する項目
#     list_display = ('id', 'title')
#     # 項目をクリックしたら詳細を閲覧できるようにリンク設定
#     list_display_links = ('id', 'title')

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name')
    list_display_links = ('id', 'item_name')

# adminサイト（http://127.0.0.1:8000/admin/） で閲覧できるように登録
# admin.site.register(Category, CategoryAdmin)
admin.site.register(Inventory, InventoryAdmin)