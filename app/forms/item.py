from django import forms
from ..models import Item

class ItemAdd(forms.ModelForm): 
    class Meta:
        model = Item
        fields = ('name','text','value', 'image')
        labels = {
            'name' : '商品名',
            'text' : '商品説明',
            'value' : '価格',
            'image' : '画像',
        }

