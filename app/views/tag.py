from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Tag, Item, User, Item_Tag, Matching
import json
from gensim.models import KeyedVectors
import operator

model_dir = "./word2vec/entity_vector.model.bin"
model = KeyedVectors.load_word2vec_format(model_dir, binary=True)

@login_required
def select_tags(request):
    tag_list = Tag.objects.values("id", "name")
    context = {
        "title": "タグ設定",
        "tag_list": tag_list,
    }
    return render(request, 'tag/select_tags.html', context)

def matching(request):
    if request.method == 'POST':
        tag_id_list = request.POST.getlist('tags')
        post_tags = []
        for tag_id in tag_id_list:
            tag = Tag.objects.get(id=tag_id)
            post_tags.append(tag.name)
        data_list = Item.objects.all()
        data = []
        for item in data_list:
            user = User.objects.get(id=item.user.id)
            if request.user == user : 
                continue
            item_tags = Item_Tag.objects.filter(item=item.id)
            matchs = Matching.objects.filter(item=item.id)
            f = False
            for match in matchs:
                print(match.seller)
                if match.seller == request.user:
                    f = True
            if f:
                continue
            count = 0
            per = 0.0
            for item_tag in item_tags:
                tag = Tag.objects.get(id=item_tag.tag.id)
                for post_tag in post_tags:
                    print(tag.name +" "+post_tag)
                    per += model.similarity(tag.name, post_tag)
                    count += 1
            per /= count
            data.append({
                "item_id" : item.id,
                "user_id" : user.id,
                "user" : user.username,
                'name' : item.name, 
                'text' : item.text, 
                'image' : item.image.url,
                'value' : item.value,
                'per' : per,
            })
        a = sorted(data, key=operator.itemgetter('per'), reverse=True)
        return render(request, 'tag/matching.html', {'items': json.dumps(a)})
    else:
        return redirect('select_tags')

def match_succes(request):
    if request.method == 'POST':
        seller=User.objects.get(id=request.user.id)
        buyer=User.objects.get(id=request.POST['user_id'])
        item=Item.objects.get(id=request.POST['item_id'])
        print(request.POST)
        match = Matching(
            seller=seller,
            buyer=buyer,
            item=item,
        )
        match.save()
        return render(request, 'tag/succes.html',{"matching":match})