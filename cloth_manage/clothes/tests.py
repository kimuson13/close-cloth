from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Wanted
# Create your tests here.
class ClothesTest(TestCase):
    def test_check(self):
        usr = User.objects.first()
        self.assertIsNotNone(usr)
        post = Post.objects.first()
        self.assertIsNotNone(post)
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        usr = cls.create_user()
    @classmethod
    def create_user(cls):
        User(username="public", password="public", is_staff=False, is_active=True).save()
        pb_usr = User.objects.filter(username="public").first()
        User(username="test", password="test", is_staff=True, is_active=True).save()
        usr = User.objects.filter(username="test").first()
        return (usr, pb_usr)
    @classmethod
    def create_post(cls, usr):
        Post(owner=usr, cloth_name='test').save()
