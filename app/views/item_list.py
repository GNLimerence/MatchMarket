from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Item

class ItemList(LoginRequiredMixin, ListView):
    template_name = "item/item_list.html"
    login_url = 'login'

    def get_queryset(self):
        # ログイン中のユーザーのみアクセス可能
        if self.request.user.is_authenticated:
            return Item.objects.filter(user=self.request.user).order_by("-created_at")
        return Item.objects.none()  # ログインしていない場合は空のクエリセットを返す
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '商品リスト'
        return context

