from rest_framework import generics

from api.models import Poll
from api.serializers import PollSerializers


class CreatePollView(generics.CreateAPIView):
    """Добавление опроса"""

    serializer_class = PollSerializers.CreatePollSerializer


class DeletePollByIdView(generics.DestroyAPIView):
    """Удаление опроса по идентификации"""

    queryset = Poll.objects.all()


class UpdatePollByIdView(generics.UpdateAPIView):
    """Обноление опроса по идентификации"""

    queryset = Poll.objects.all()
    serializer_class = PollSerializers.UpdatePollSerializer


class GetPollView(generics.ListAPIView):
    """Вывод всех опросов"""

    queryset = Poll.objects.all()
    serializer_class = PollSerializers.GetPollSerializer


class GetActivePollView(generics.ListAPIView):
    """Вывод активных опросов"""

    queryset = Poll.objects.filter(is_active=True)
    serializer_class = PollSerializers.GetPollSerializer


class FindPollByIdView(generics.RetrieveAPIView):
    """Поиск опроса по идентификации"""

    queryset = Poll.objects.all()
    serializer_class = PollSerializers.GetPollSerializer


class FindActivePollByIdView(generics.RetrieveAPIView):
    """Поиск активного опроса по идентификации"""

    queryset = Poll.objects.filter(is_active=True)
    serializer_class = PollSerializers.GetPollSerializer
