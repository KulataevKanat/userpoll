from django.contrib import admin

from api.models import User, Poll, Question, PollWork, QuestionHistory, PollHistory

admin.site.register(User)
admin.site.register(PollWork)
admin.site.register(Poll)
admin.site.register(PollHistory)
admin.site.register(Question)
admin.site.register(QuestionHistory)
