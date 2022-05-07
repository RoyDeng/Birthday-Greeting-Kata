from django.test import TestCase
from rest_framework import status
from rest_framework.test import (
    APITestCase, APIRequestFactory, force_authenticate
)
from rest_framework.test import APIClient
from datetime import datetime

from api.models import Member

# Create your tests here.

class MemberTestCase(APITestCase):
    def setUp(self):
        members = [
            {
                "first_name": "Robert",
                "last_name": "Yen",
                "gender": 1,
                "date_of_birth": "1985-08-08",
                "email": "robert.yen@linecorp.com"
            },
            {
                "first_name": "Cid",
                "last_name": "Change",
                "gender": 1,
                "date_of_birth": "1990-10-10",
                "email": "cid.change@linecorp.com"
            },
            {
                "first_name": "Miki",
                "last_name": "Lai",
                "gender": 2,
                "date_of_birth": "1993-04-05",
                "email": "miki.lai@linecorp.com"
            },
            {
                "first_name": "Sherry",
                "last_name": "Chen",
                "gender": 2,
                "date_of_birth": "1993-08-08",
                "email": "sherry.lai@linecorp.com"
            },
            {
                "first_name": "Peter",
                "last_name": "Wang",
                "gender": 1,
                "date_of_birth": "1950-12-22",
                "email": "peter.wang@linecorp.com"
            },
        ]

        for member in members:
            Member.objects.create(
                first_name=member["first_name"],
                last_name=member["last_name"],
                gender=member["gender"],
                date_of_birth=member["date_of_birth"],
                email=member["email"]
            )

    def check_members_brithday_is_correct(self, messages):
        for message in messages:
            try:
                member = Member.objects.get(email=message["email"])

                try:
                    self.assertEqual(member.date_of_birth.month, 8)
                except AssertionError:
                    self.fail("Birthday month is incorrect")

                try:
                    self.assertEqual(member.date_of_birth.day, 8)
                except AssertionError:
                    self.fail("Birthday day is incorrect")
            except Member.DoesNotExist:
                self.fail("Member with email: {email} not found".format(email=message["email"]))

    def test_returns_200_status_code_when_getting_messages(self):
        client = APIClient()
        response = client.get("/api/members/", {"date": "08-08"})

        self.check_members_brithday_is_correct(response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
