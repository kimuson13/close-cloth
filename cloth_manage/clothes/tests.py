from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Wanted
import datetime, random
from PIL import Image, ImageDraw, ImageFont
# Create your tests here.
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0), (255, 255, 255)]
def get_image(n):
    screen = (200, 200)
    pen_color = random.choice(colors)
    bg_color = random.choice(colors)
    img = Image.new('RGB', screen, bg_color)
    x, y = img.size
    u = x - 1
    v = y - 1
    draw = ImageDraw.Draw(img)
    draw.line((0, 0, u, 0), pen_color)
    filename = "/sample_{}.jpg".format(n)
    img.save("media"+filename)
    return filename
class ClothesTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        usr= cls.create_user()
        cls.create_post(usr)
        cls.create_wish(usr)
    @classmethod
    def create_user(cls):
        User(username="test", password="test", is_staff=True, is_active=True).save()
        usr = User.objects.filter(username='test').first()
        return(usr)
    @classmethod
    def create_post(cls, usr):
        Post(owner=usr, cloth_name='test', item_info=1, brand_name='test', season='test', cloth_size='test', \
            material='test', price=1, buying_place='test', buying_date=datetime.date.today(), post_images=get_image(1)).save()
        Post(owner=usr, cloth_name='test2', item_info=1, brand_name='test2', season='test2', cloth_size='test2', \
            material='test2', price=1, buying_place='test2', buying_date=datetime.date.today(), post_images=get_image(2)).save()
        Post(owner=usr, cloth_name='test3', item_info=1, brand_name='test3', season='test3', cloth_size='test3', \
            material='test3', price=1, buying_place='test3', buying_date=datetime.date.today(), post_images=get_image(3)).save()
        Post(owner=usr, cloth_name='test4', item_info=1, brand_name='test4', season='test4', cloth_size='test4', \
            material='test4', price=1, buying_place='test4', buying_date=datetime.date.today(), post_images=get_image(4)).save()
    @classmethod
    def create_wish(cls, usr):
        Wanted(owner=usr, wanted_cloth_name='test', wanted_brand_name='test', wanted_season='test', wanted_price=1, \
            priority=1, wanted_images=get_image(5)).save()
        Wanted(owner=usr, wanted_cloth_name='test2', wanted_brand_name='test2', wanted_season='test2', wanted_price=1, \
            priority=1, wanted_images=get_image(6)).save()
        Wanted(owner=usr, wanted_cloth_name='test3', wanted_brand_name='test3', wanted_season='test3', wanted_price=1, \
            priority=1, wanted_images=get_image(7)).save()
    def test_check(self):
        usr = User.objects.first()
        self.assertIsNotNone(usr)
        post = Post.objects.first()
        self.assertIsNotNone(post)
        wish = Wanted.objects.first()
        self.assertIsNotNone(wish)
        self.assertEquals(usr, post.owner, wish.owner)
        c1 = Post.objects.all().count()
        c2 = Wanted.objects.all().count()
        self.assertIs(c1, 4)
        self.assertIs(c2, 3)