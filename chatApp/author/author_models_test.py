from django.test import TestCase
from .models import UserDetails, User


class UserDetailsTestCase(TestCase):
  def setUp(self):
    user = User.objects.create_user(username='test_username', 
                                    email='test_email@gmail.com',
                                    password='test_password')
    UserDetails.objects.create(user=user, gender='test_gender')
  
  def test_userdetails_gender(self):
    user = User.objects.get(username='test_username')
    userDet = UserDetails.objects.get(user=user)
    self.assertEqual(userDet.gender,'test_gender')

