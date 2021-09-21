from django.urls import path
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny

from api.authentication import SafeJWTAuthentication
from api.views import UserViews, GroupViews, PollViews, PollWorkViews, QuestionViews

urlpatterns = [
    # POLL WORK
    path("poll_work/work/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(PollWorkViews.CreatePollWorkView)).as_view()),
    path("poll_work/find_all_poll_works/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(PollWorkViews.GetPollWorkView)).as_view()),
    path("poll_work/find_poll_work_by_userId/<int:user_id>",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(PollWorkViews.FindPollWorkByUserIdView)).as_view()),

    # POLL
    path("poll/create_poll/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(PollViews.CreatePollView)).as_view()),
    path("poll/delete_poll_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(PollViews.DeletePollByIdView)).as_view()),
    path("poll/update_poll_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(PollViews.UpdatePollByIdView)).as_view()),
    path("poll/find_all_polls/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(PollViews.GetPollView)).as_view()),
    path("poll/find_all_active_polls/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(PollViews.GetActivePollView)).as_view()),
    path("poll/find_poll_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(PollViews.FindPollByIdView)).as_view()),
    path("poll/find_active_poll_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(PollViews.FindActivePollByIdView)).as_view()),

    # QUESTION
    path("question/create_question/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(QuestionViews.CreateQuestionView)).as_view()),
    path("question/delete_question_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(QuestionViews.DeleteQuestionByIdView)).as_view()),
    path("question/update_question_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(QuestionViews.UpdateQuestionByIdView)).as_view()),
    path("question/find_all_questions/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(QuestionViews.GetQuestionView)).as_view()),
    path("question/find_question_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(QuestionViews.FindQuestionByIdView)).as_view()),

    # USERS
    path("user/access_token/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.AccessToken)).as_view()),
    path("user/refresh_token/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.RefreshToken)).as_view()),
    path("user/create_user/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.CreateUserView)).as_view()),
    path("user/create_super_user/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.CreateSuperUserView)).as_view()),
    path("user/delete_user_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.DeleteUserByIdView)).as_view()),
    path("user/delete_all_users/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.DeleteAllUsersView)).as_view()),
    path("user/update_user_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.UpdateUserView)).as_view()),
    path("user/find_all_users/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.GetUserView)).as_view()),
    path("user/find_user_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.FindUserByIdView)).as_view()),

    # GROUPS
    path("group/create_group/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(GroupViews.CreateGroupView)).as_view()),
    path("group/delete_group_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(GroupViews.DeleteGroupByIdView)).as_view()),
    path("group/update_group_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(GroupViews.UpdateGroupByIdView)).as_view()),
    path("group/find_all_groups/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(GroupViews.GetGroupView)).as_view()),
    path("group/find_group_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(GroupViews.FindGroupByIdView)).as_view()),
]
