from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    sex_data = [
        (1, '男'),
        (2, '女'),
        (3, 'その他'),
    ]
    date_joined = None
    first_name = None
    last_name = None
    sex = models.IntegerField(choices=sex_data)
    birthday = models.DateField()
    adress = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ["sex", "birthday"]
    
    class Meta:
        verbose_name_plural = 'User'


class Item(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    name = models.CharField(max_length=255)
    text = models.TextField()
    value = models.IntegerField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(null=True, upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Item'

class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Tag'

class Item_Tag(models.Model):
    item = models.ForeignKey(Item, on_delete = models.PROTECT)
    tag = models.ForeignKey(Tag, on_delete = models.PROTECT)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["item_id", "tag_id"],
                name="item_tag_unique"
            ),
        ]
    def __str__(self):
        return f"{self.item_id} {self.tag_id}"
    
    class Meta:
        verbose_name_plural = 'Item_Tag'

class Matching(models.Model):
    seller = models.ForeignKey(User, on_delete = models.PROTECT, related_name='seller_user')
    buyer = models.ForeignKey(User, on_delete = models.PROTECT, related_name='buyer_user')
    item = models.ForeignKey(Item, on_delete = models.PROTECT)
    matching_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Matching'
        constraints = [
            models.UniqueConstraint(
                fields=["buyer_id", "item_id"],
                name="buyer_item_unique",
            ),
        ]
    
    def __str__(self):
        return f"{self.item_id} {self.buyer_id}"

class Chat(models.Model):
    matching_id = models.ForeignKey(Matching, on_delete = models.PROTECT)
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    #receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
    message = models.TextField()
    sented_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.sender_id} {self.sented_at}"
    class Meta:
        verbose_name_plural = 'Chat'

class Review(models.Model):
    rater = models.ForeignKey(Matching, on_delete = models.PROTECT, related_name='rater_user')
    evaluator = models.ForeignKey(Matching, on_delete = models.PROTECT, related_name='evaluator_user')
    score = models.IntegerField()
    text = models.TextField()
    class Meta:
        verbose_name_plural = 'Review'
        constraints = [
            models.UniqueConstraint(
                fields=["rater_id", "evaluator_id"],
                name="rater_evaluator_unique",
            ),
        ]
    def __str__(self):
        return f"{self.evaluator_id} {self.score}"
    