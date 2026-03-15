from django.forms import ModelForm
from .models import Inventory

class InventoryForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        
        Attributes:
        model: モデルのクラス
        fields: フォームで使用するモデルのフィールドを指定
        '''
        model = Inventory
        # created_at や updated_at はいらない ⇒ それらは自動入力され、ユーザ－に入力して欲しいものではないから
        fields = ['item_name', 'unit_price', 'inventory_quantity', 'description', 'image1', 'part_number']