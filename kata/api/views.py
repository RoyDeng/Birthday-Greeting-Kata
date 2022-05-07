import sys
import os
import json
import uuid
from enum import Enum
import asyncio

from pyppeteer import launch

import requests


from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django_redis import get_redis_connection

from api.models import Member
from api.serializers import MemberSerializer
from dx_logger import logger
from api.pagination import MemberPagination

from datetime import date, datetime, timedelta
import calendar
from django.core.cache import cache
from hashlib import sha1
import moment

from django.template.loader import render_to_string

class MemberList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        pagination = MemberPagination()
        members = Member.objects.all()
        members = pagination.paginate_queryset(
            queryset=members,
            request=request
        )

        messages = []

        for member in members:
            if member.age > 49:
                messages.append({
                    "email": member.email,
                    "subject": "Happy birthday!",
                    "message": "Happy birthday, dear `{first_name}`!".format(
                        first_name=member.first_name
                    ),
                    "picture": "https://scontent.ftpe15-1.fna.fbcdn.net/v/t1.6435-9/173822014_801912067086569_6354124022379710057_n.jpg?_nc_cat=100&ccb=1-6&_nc_sid=730e14&_nc_ohc=Ez4EXqHzALUAX-c15yj&_nc_ht=scontent.ftpe15-1.fna&oh=00_AT_v4wjNbvpEojVwl5xkDHI4TBL8gAZZ8A03MLjlxfmnyA&oe=629B5D03"
                })

        return Response(messages)
