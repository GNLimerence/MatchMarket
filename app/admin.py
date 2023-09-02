from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .models import User
from .models import Item
from .models import Tag
from .models import Item_Tag
from .models import Chat
from .models import Matching
from .models import Review
# Register your models here.
User = get_user_model()
admin.site.register(User)
admin.site.register(Item)
admin.site.register(Tag)
admin.site.register(Item_Tag)
admin.site.register(Chat)
admin.site.register(Matching)
admin.site.register(Review)
admin.site.unregister(Group) 