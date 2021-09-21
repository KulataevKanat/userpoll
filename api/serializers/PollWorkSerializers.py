from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from api.models import PollWork
from api.serializers import PollSerializers


class CreatePollWorkSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    """Опрос пользователя"""

    poll_history_id = PollSerializers.CreatePollHistorySerializer(many=True, allow_null=True)

    class Meta:
        model = PollWork
        fields = [
            'id',
            'user_id',
            'is_anonymity',
            'poll_id',
            'poll_history_id',
        ]


class GetPollWorkSerializer(serializers.ModelSerializer):
    """Вывод опросов пользователей"""

    poll_history_id = PollSerializers.CreatePollHistorySerializer(many=True, allow_null=True)

    class Meta:
        model = PollWork
        fields = [
            'id',
            'user_id',
            'is_anonymity',
            'poll_history_id',
        ]
