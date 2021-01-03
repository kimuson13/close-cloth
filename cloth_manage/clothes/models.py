from django.db import models
from django.contrib.auth.models import User
# Create your models here.
ITEM_CHOICES = (
    (1, 'Tops'),
    (2, 'Pants'),
    (3, 'Outers'),
    (4, 'SetUp'),
    (5, 'Coats'),
    (6, 'Shoes'),
    (7, 'Accessories'),
    (8, 'Belts'),
    (9, 'Bags'),
    (10, 'Others')
)

PRIORITY_CHOICES = (
    (1, '優先度1'),
    (2, '優先度2'),
    (3, '優先度3'),
    (4, '優先度4'),
    (5, '優先度5')
)

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    cloth_name = models.CharField(max_length=40)
    item_info = models.IntegerField(choices=ITEM_CHOICES)
    brand_name = models.CharField(max_length=40)
    season = models.CharField(max_length=7)
    cloth_size = models.CharField(max_length=8)
    material = models.CharField(max_length=40)
    price = models.PositiveIntegerField()
    buying_place = models.CharField(max_length=20)
    buying_date = models.DateField(
        verbose_name='購入日時',
        blank=True,
        null=True,
    )
    post_images = models.ImageField(upload_to='media')
    def __str__(self):
        return str(self.cloth_name) + '(' + str(self.owner) + ')'

class Wanted(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='want_owner')
    wanted_cloth_name = models.CharField(max_length=40)
    wanted_brand_name = models.CharField(max_length=40)
    wanted_season = models.CharField(max_length=7)
    wanted_price = models.PositiveIntegerField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    wanted_images = models.ImageField(upload_to='media')
    def __str__(self):
        return str(self.wanted_cloth_name) + '(' + str(self.owner) + ')'




