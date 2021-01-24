from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Wanted
import datetime
from PIL import Image, ImageDraw, ImageFont
# Create your tests here.
def get_image():
    screen = (200, 200)
    pen_color = (255, 0, 0)
    bg_color = (0, 255, 0)
    img = Image.new('RGB', screen, bg_color)
    x, y = img.size
    u = x - 1
    v = y - 1
    draw = ImageDraw.Draw(img)
    draw.line((0, 0, u, 0), pen_color)
    filename = "/sample.jpg"
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
            material='test', price=1, buying_place='test', buying_date=datetime.date.today(), post_images=get_image()).save()
    @classmethod
    def create_wish(cls, usr):
        Wanted(owner=usr, wanted_cloth_name='test', wanted_brand_name='test', wanted_season='test', wanted_price=1, \
            priority=1, wanted_images=get_image()).save()
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
        self.assertIs(c1, 1)
        self.assertIs(c2, 1)