from django.test import TestCase
from models import User
from django.core.exceptions import FieldError
class TEST(TestCase):
    def setUp(self):
        User.objects.create(name="Ahmed",properties={"city":"Giza","Address":{"district":"Ahram","Code":11263}})
        User.objects.create(name="Mohamed",properties={"city":"Cairo","Address":{"district":"Helipolis","Code":11351}})

    def test_animals_can_speak(self):
        q = User.objects.filter(properties__has="$.city=Giza")
        self.assertEqual(q[0].name,"Ahmed")
        q= User.objects.filter(properties__has="$.Address.Code = 11351")
        self.assertEqual(q[0].name,"Mohamed")
        try:
            User.objects.filter(name__has="Ahmed")
            self.assertEqual(1, 0)
        except FieldError as exp:
                self.assertEqual(1,1)

