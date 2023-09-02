from django.core.management.base import BaseCommand
from ...models import Item
from ...models import User
from ...models import Tag
from ...models import Item_Tag
import random
import os
import environ
from pathlib import Path

class Command(BaseCommand):
    help = "サンプルデータの作成"

    def handle(self, *args, **options):
                
        BASE_DIR = Path(__file__).resolve().parent.parent
        env = environ.Env()
        env.read_env(os.path.join(BASE_DIR, '.env'))
        adminname = env('ADMIN_USERNAME')
        adminpass = env('ADMIN_PASSWORD')
        admin = User(
            username=adminname,
            sex=1,
            birthday="2000-01-01",
            is_staff = True,
            is_superuser = True
        )
        admin.set_password(adminpass)
        admin.save()
        for i in range(20):
            username = "user" + str(i)
            password = "username" + str(i)
            user = User(
                username=username,
                sex=1,
                birthday="2000-01-01"
            )
            user.set_password(password)
            user.save()

        tag_array = ["小説", "服", "家具", "アウトドア", "靴", "参考書", "漫画", "パソコン", "アクセサリー", "アート"]
        for i in tag_array:
            tag = Tag(
                name = i,
            )
            tag.save()

        tmp = 0
        img = 0
        for i in range(20):
            user = User.objects.get(username="user" + str(i))
            for j in range(random.randint(0, 3)):
                item = Item(
                    name = "item"+str(i) + "-" + str(j),
                    user = user,
                    text = "item"+str(i) + "-" + str(j),
                    image = "images/sample_"+str(img)+".jpg",
                    value = i * 1000 + 1000,
                )
                item.save()
                for k in range(random.randint(2,5)):
                    item = Item.objects.get(name="item"+str(i) + "-" + str(j))
                    tag = Tag.objects.get(name=tag_array[tmp])
                    item_tag = Item_Tag(
                        item = item,
                        tag = tag,
                    )
                    tmp += 1
                    tmp %= 10
                    img += 1
                    img %= 3
                    item_tag.save()



