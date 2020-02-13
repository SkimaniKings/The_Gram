from django.test import TestCase
from .models import Profile, Image,Post,User

# Create your tests here.

class ImageTest(TestCase):
    def setUp(self):
        self.new_user = User(username='simonking', email='simonking@gmail.com', password='mynameiskimani1234')
        self.new_user.save()
       
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, User))
        
        
