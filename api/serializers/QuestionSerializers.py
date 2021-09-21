from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from api.models import Question, QuestionHistory


class CreatePollQuestionSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    """Добавление вопроса к опросу"""

    class Meta:
        ref_name = "Question Serializer"
        model = Question
        fields = [
            'id',
            'name',

        ]


class AllQuestionSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    """Добавление|Изменение вопроса к опросу по идентификации"""

    class Meta:
        model = Question
        fields = [
            'id',
            'name',
            'poll_questions',

        ]


class CreatePollQuestionHistorySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    """Добавление истории вопроса к истории опроса"""

    class Meta:
        ref_name = "QuestionHistory Serializer"
        model = QuestionHistory
        fields = [
            'id',
            'name',
            'text',
            'type',
            'answer',

        ]


class GetQuestionSerializer(serializers.ModelSerializer):
    """Вывод вопросов"""

    class Meta:
        model = Question
        fields = [
            'id',
            'name',
        ]
