from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Wanted
import datetime, io
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
# Create your tests here.
def get_image_dict():
        img_file = io.StringIO()
        img = Image.new('RGBA', size=(10,10), color=(255, 255, 255))
        img.save(img_file, 'jpeg')
        img_file.name = 'test_img.jpeg'
        img_file.seek(0)
        img_dict = {
            'image': SimpleUploadedFile(
                img_file.name,
                img_file.read(),
                content_type='media'
            )
        }
        return img_dict
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
            material='test', price=1, buying_place='test', buying_date=datetime.date.today(), post_images=get_image_dict()).save()
    @classmethod
    def create_wish(cls, usr):
        Wanted(owner=usr, wanted_cloth_name='test', wanted_brand_name='test', wanted_season='test', wanted_price=1, \
            priority=1, wanted_images=get_image_dict()).save()
    def test_check(self):
        usr = User.objects.first()
        self.assertIsNotNone(usr)
        post = Post.objects.first()
        self.assertIsNotNone(post)
        wish = Wanted.objects.first()
        self.assertIsNotNone(wish)