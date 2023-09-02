from django.urls import path
from .views import top
from .views import item_list
from .views import user
from .views import item
from .views import chat
from .views import tag
from .views import item_update
from .views import user_review

urlpatterns = [
    path("", top.index, name="index"),
    path("login", user.login_user, name = "login"),
    path("logout", user.logout_user, name = "logout"),
    path("register", user.register_user, name = "register"),
    path("item_list/", item_list.ItemList.as_view(), name="item_list"),
    path("item/add", item.item_add, name="item_add"),
    path('chat/<matching_id>',chat.chat,name='chat'),
    path("item/tag/<int:item_id>", item.item_tag_add, name="item_tag_add"),
    path("select_tags/", tag.select_tags, name="select_tags"),
    path('item_list/<int:pk>/', item_update.ItemUpdateView.as_view(), name='item_edit'),
    path('rate/<int:matching_id>', user_review.rate_seller, name='rate_seller'),
    path('match', tag.matching, name='match'),
    path('match/succes', tag.match_succes, name='match_succes'),
    path('item_list/<int:pk>/edit', item_update.ItemUpdateView.as_view(), name='item_edit'),
    path('chathomepage/', chat.MatchingPage, name='chathomepage'),
]