from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response

from api.models import Question, Poll
from api.serializers import QuestionSerializers
from userpoll.advice import DATA_DETAIL, CREATE_POLL_DATE_ACTIVE, DELETE_POLL_DATE_ACTIVE, UPDATE_POLL_DATE_ACTIVE


class CreateQuestionView(generics.CreateAPIView):
    """Добавление вопроса"""

    serializer_class = QuestionSerializers.AllQuestionSerializer

    def get_poll(self, pk=None):
        try:
            return Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            raise Http404

    def post(self, request, *args, **kwargs):
        """Метод добавления вопроса"""

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            poll = self.get_poll(pk=request.data['poll_questions'])
            if poll.start_date is not None:
                return Response({DATA_DETAIL: CREATE_POLL_DATE_ACTIVE}, status=status.HTTP_403_FORBIDDEN)
            else:
                self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeleteQuestionByIdView(generics.DestroyAPIView):
    """Удаление вопроса по идентификации"""

    queryset = Question.objects.all()

    def get_poll(self, pk=None):
        try:
            return Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            raise Http404

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        poll = self.get_poll(pk=instance.poll_questions.id)
        if poll.start_date is not None:
            return Response({DATA_DETAIL: DELETE_POLL_DATE_ACTIVE}, status=status.HTTP_403_FORBIDDEN)
        else:
            self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateQuestionByIdView(generics.UpdateAPIView):
    """Обноление вопроса по идентификации"""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializers.AllQuestionSerializer

    def get_poll(self, pk=None):
        try:
            return Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            raise Http404

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        poll = self.get_poll(pk=instance.poll_questions.id)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid(raise_exception=True):
            if poll.start_date is not None:
                return Response({DATA_DETAIL: UPDATE_POLL_DATE_ACTIVE}, status=status.HTTP_403_FORBIDDEN)
            else:
                self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class GetQuestionView(generics.ListAPIView):
    """Вывод вопросов"""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializers.GetQuestionSerializer


class FindQuestionByIdView(generics.RetrieveAPIView):
    """Поиск вопроса по идентификации"""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializers.GetQuestionSerializer
