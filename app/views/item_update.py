from django.views.generic import UpdateView
from django.urls import reverse
from ..models import Item
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin


class ItemForm(forms.ModelForm):
    name = forms.CharField(label="商品名")
    text = forms.CharField(label="商品説明", widget=forms.Textarea)
    value = forms.IntegerField(label="価格")
    image = forms.ImageField(label="画像")
    class Meta:
        model = Item
        fields = ['name', 'text', 'value', 'image']  # 必要なフィールドのみを指定

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"



class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item/item_update.html'
    login_url = 'login'
    
    # ログイン中のユーザーのみアクセス可能
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
    def get_success_url(self):
        return reverse("item_tag_add", args=[str(self.object.pk)])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '商品編集'
        return context