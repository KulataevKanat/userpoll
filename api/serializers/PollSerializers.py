from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from api.models import Poll, PollHistory
from api.serializers import QuestionSerializers


class CreatePollSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    """Добавление опроса"""

    poll_questions = QuestionSerializers.CreatePollQuestionSerializer(many=True, allow_null=True)

    class Meta:
        model = Poll
        fields = [
            'id',
            'name',
            'is_active',
            'poll_questions',
            'start_date',
            'expiration_date',
        ]


class UpdatePollSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    """Обновление опроса"""

    class Meta:
        model = Poll
        fields = [
            'id',
            'name',
            'is_active',
            'start_date',
            'expiration_date',
        ]


class CreatePollHistorySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    """Добавление истории опроса"""

    poll_history_questions = QuestionSerializers.CreatePollQuestionHistorySerializer(many=True, allow_null=True)

    class Meta:
        model = PollHistory
        fields = [
            'id',
            'name',
            'is_active',
            'start_date',
            'expiration_date',
            'poll_history_questions',
        ]


class GetPollSerializer(serializers.ModelSerializer):
    """Вывод опросов"""

    poll_questions = QuestionSerializers.GetQuestionSerializer(many=True)

    class Meta:
        model = Poll
        ref_name = "Get poll serializer"
        fields = [
            'id',
            'name',
            'is_active',
            'start_date',
            'expiration_date',
            'poll_questions',

        ]
