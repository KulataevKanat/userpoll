from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response

from api.models import Poll, PollWork
from api.serializers import PollWorkSerializers
from userpoll.advice import ONE_OPTION, YES, NO, MANY_OPTIONS, ANSWER_NONE, TEXT, TYPE_NONE


class CreatePollWorkView(generics.CreateAPIView):
    """Работа пользователя с опросом"""

    serializer_class = PollWorkSerializers.CreatePollWorkSerializer

    def get_poll(self, pk=None):
        try:
            return Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            raise Http404

    def post(self, request, *args, **kwargs):
        """Метод работы пользователя с опросом"""

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            for poll_history in request.data['poll_history_id']:
                poll = self.get_poll(pk=request.data['poll_id'])
                poll_history['name'] = poll.name
                poll_history['is_active'] = poll.is_active
                poll_history['start_date'] = poll.start_date
                poll_history['expiration_date'] = poll.expiration_date
                poll_questions_name = [poll_questions.name for poll_questions in poll.poll_questions.all()]

                for question_history, names in zip(poll_history['poll_history_questions'], poll_questions_name):
                    question_history['name'] = names
                    if question_history['answer'].__eq__(YES) and question_history['text'] is None:
                        question_history['type'] = ONE_OPTION

                    elif question_history['answer'].__eq__(NO) and question_history['text'] is None:
                        question_history['type'] = ONE_OPTION

                    elif question_history['text'] is not None and question_history['answer'].__eq__(ANSWER_NONE):
                        question_history['type'] = TEXT

                    elif question_history['answer'].__eq__(YES) or question_history['answer'].__eq__(NO) and \
                            question_history['text'] is not None:
                        question_history['type'] = MANY_OPTIONS

                    elif question_history['answer'] is None and question_history['text'] is None:
                        question_history['type'] = TYPE_NONE

                if request.data['user_id'] is None:
                    self.perform_create(serializer, True)
                else:
                    self.perform_create(serializer, False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer, is_bool=None):
        serializer.save(is_anonymity=is_bool)


class GetPollWorkView(generics.ListAPIView):
    """Вывод всех пройденных опросов"""

    queryset = PollWork.objects.all()
    serializer_class = PollWorkSerializers.GetPollWorkSerializer


class FindPollWorkByUserIdView(generics.RetrieveAPIView):
    """Вывод всех пройденных опросов определенного пользователя"""

    queryset = PollWork.objects.all()
    serializer_class = PollWorkSerializers.GetPollWorkSerializer

    def get_object(self, user_id=None):
        try:
            return PollWork.objects.get(user_id=user_id)
        except PollWork.DoesNotExist:
            raise Http404

    def retrieve(self, request, user_id=None, *args, **kwargs):
        instance = self.get_object(user_id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
