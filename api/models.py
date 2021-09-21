from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.managers import UserAccountManager
from userpoll import settings
from userpoll.advice import TYPE_NONE, TEXT, ONE_OPTION, MANY_OPTIONS, NO, ANSWER_NONE, YES
from userpoll.models import BaseModel


def role_null():
    return Group.objects.get_or_create(name='role_null')[0]


class User(BaseModel, AbstractUser):
    groups = models.ForeignKey(Group, on_delete=models.SET(role_null), null=True, blank=True)
    email = models.EmailField(max_length=50, unique=False, blank=True, null=True)

    objects = UserAccountManager()

    REQUIRED_FIELDS = ['groups_id', 'email']
    USERNAME_FIELD = 'username'
    REQUIRED_ADMIN_FIELDS = ['email']

    def __str__(self):
        return self.username.__str__()

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    class Meta:
        db_table = 'api_user'
        verbose_name = _('Пользоваетель')
        verbose_name_plural = _('Пользователи')


class Poll(BaseModel):
    name = models.CharField(max_length=80, blank=True)
    description = models.TextField(max_length=5000, blank=True, default="poll_description")
    is_active = models.BooleanField(_('active'), default=True)
    start_date = models.DateTimeField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _('Опрос')
        verbose_name_plural = _('Опросы')


class Question(BaseModel):
    name = models.CharField(max_length=80, blank=True)
    poll_questions = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True, blank=True,
                                       related_name="poll_questions")

    class Meta:
        verbose_name = _('Вопрос')
        verbose_name_plural = _('Вопросы')


class PollWork(BaseModel):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    poll_id = models.ForeignKey(Poll, on_delete=models.PROTECT, null=True, blank=True,
                                related_name="poll_id")
    is_anonymity = models.BooleanField(_('active'), default=False)

    class Meta:
        verbose_name = _('Сдача опроса пользователем')
        verbose_name_plural = _('Сдача опроса пользователем')


class PollHistory(BaseModel):
    name = models.CharField(max_length=80, blank=True)
    description = models.TextField(max_length=5000, blank=True, default="poll_description")
    is_active = models.BooleanField(_('active'), default=True)
    poll_history_id = models.ForeignKey(PollWork, on_delete=models.PROTECT, null=True, blank=True,
                                        related_name="poll_history_id")
    start_date = models.DateTimeField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _('История опроа')
        verbose_name_plural = _('История опросов')


class QuestionHistory(BaseModel):
    QUESTION_TYPE = (
        (TYPE_NONE, _(TYPE_NONE)),
        (TEXT, _(TEXT)),
        (ONE_OPTION, _(ONE_OPTION)),
        (MANY_OPTIONS, _(MANY_OPTIONS)),
    )
    ANSWERS = (
        (ANSWER_NONE, _(ANSWER_NONE)),
        (YES, _(YES)),
        (NO, _(NO)),
    )
    name = models.CharField(max_length=80, blank=True)
    text = models.TextField(max_length=5000, blank=True, null=True)
    type = models.CharField(choices=QUESTION_TYPE, max_length=100, blank=True, null=True,
                            default=TYPE_NONE)
    answer = models.CharField(choices=ANSWERS, max_length=100, blank=True, null=False,
                              default=ANSWER_NONE)
    poll_history_questions = models.ForeignKey(PollHistory, on_delete=models.CASCADE, null=True, blank=True,
                                               related_name="poll_history_questions")

    class Meta:
        verbose_name = _('История вопроса')
        verbose_name_plural = _('История Вопросов')
