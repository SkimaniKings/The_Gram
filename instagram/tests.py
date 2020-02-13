from django.test import TestCase
from .models import Profile, Image,Post,User

# Create your tests here.

class ImageTest(TestCase):
    def setUp(self):
        self.new_user = User(username='simonking', email='simonking@gmail.com', password='mynameiskimani1234')
        self.new_user.save()
        self.new_image = Image(name='Ronaldo', image='ronaldo.jpg', caption='King of Football',  like_add=0)
       
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, User))
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
    
    def test_delete_image(self):
        self.new_image.save_image()
        self.new_image.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image)==0)
        
        
class ProfileTest(TestCase):
    
    def setUp(self):
        self.new_user = User(username='simonking', email='simonking@gmail.com', password='mynameiskimani12234')
        self.new_user.save()
        self.new_profile = Profile(image='ronaldo.jpg',  user=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))
        
    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)
    
    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)==0)