from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        read_only=True
    )
    first_name = serializers.CharField(
        required=True,
        max_length=100
    )
    last_name = serializers.CharField(
        required=True,
        max_length=100
    )

    class Meta:
        model = Member
        fields = [
            "id",
            "first_name",
            "last_name"
        ]
