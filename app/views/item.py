from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Item
from ..models import User
from ..models import Tag
from ..models import Item_Tag
from ..forms.item import ItemAdd

@login_required
def item_add(request):
    if request.POST:
        user = User.objects.get(id=request.user.id)
        form = ItemAdd(request.POST, request.FILES)
        item = form.save(commit=False)
        item.user = user
        item.save()
        context = {
            "title": "追加処理完了",
        }

        return redirect('item_tag_add', item_id = item.id)
    context = {
        "title": "商品追加",
        "form": ItemAdd()
    }
    return render(request, "item/add.html", context)

@login_required
def item_tag_add(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.user.id != item.user.id :
        context = {
        "title": "エラー",
        "message": "ユーザーが正しくありません",
        }
        return render(request, "message.html", context)
    if request.POST :
        tag_id_list = request.POST.getlist('tag_list')
        for tag_id in tag_id_list:
            print(tag_id)
            tag = Tag.objects.get(id=tag_id)
            item_tag = Item_Tag(
                item = item,
                tag = tag,
            )
            print(item_tag)
            item_tag.save()
        return redirect("item_list")
        
    tag_list = Tag.objects.values("id", "name")
    context = {
        "title": "タグ登録",
        "tag_list": tag_list,
    }
    return render(request, "item/tag.html", context)