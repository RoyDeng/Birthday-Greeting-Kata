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
        date = self.request.query_params.get("date", "")

        if date == "":
            return Response("Date is null", status=status.HTTP_400_BAD_REQUEST)

        try:
            datetime.strptime(date, "%m-%d")
        except ValueError:
            return Response("Not date format", status=status.HTTP_400_BAD_REQUEST)

        month = int(date.split("-")[0])
        day = int(date.split("-")[1])

        pagination = MemberPagination()
        members = Member.objects.filter(
            date_of_birth__month=month,
            date_of_birth__day=day
        )
        members = pagination.paginate_queryset(
            queryset=members,
            request=request
        )

        messages = []

        for member in members:
            messages.append({
                "Subject: Happy birthday!"
            })
            messages.append({
                "Happy birthday, dear {first_name}!".format(
                    first_name=member.first_name
                )
            })

        return Response(messages)
