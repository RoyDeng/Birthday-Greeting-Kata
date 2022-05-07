"""Django crontab."""
import logging
import json
from redis import StrictRedis
from django.conf import settings
import pygsheets
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)

NOTIFICATIONS_CONN = get_redis_connection("reservation_notifications")

GS = pygsheets.authorize(service_file=settings.GOOGLE_AUTH_FILE)


def update_api_reservation_notifications_from_googlesheet():
    sht = GS.open_by_url(
        "https://docs.google.com/spreadsheets/d/1jXzCXILwBJ0Oe8uXXHAokRtsDUPhAqQhXo1wEfEoakQ"
    )

    wks = sht.worksheet_by_title("預約網紅")
    emails = []

    for f in wks.get_all_records():
        emails.append(f["email"])

    NOTIFICATIONS_CONN.set(wks.title, json.dumps(emails))

    logger.info(f"notifications loaded...")
