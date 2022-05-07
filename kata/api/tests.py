from django.test import TestCase

from api.models import Member

# Create your tests here.

class MemberTestCase(APITestCase):
    def setUp(self):
        member = Member.objects.create(
            username="admin",
            email="admin@dailyview.tw",
            password="big12345"
        )
