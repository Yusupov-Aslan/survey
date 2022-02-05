from django.urls import path

from survey.views import (
    PollView, AddPollView, PollDetailView, PollUpdateView, PollDeleteView, ChoiceCreateView, ChoiceUpdateView,
    ChoiceDeleteView, AnswerPollView, AnswersListView
)


urlpatterns = [
    path('', PollView.as_view(), name='polls_view'),
    path('new_poll/', AddPollView.as_view(), name='add_poll_view'),
    path('poll/<int:pk>/', PollDetailView.as_view(), name='detail_view'),
    path('poll/<int:pk>/update/', PollUpdateView.as_view(), name='update_poll_view'),
    path('poll/<int:pk>/delete/', PollDeleteView.as_view(), name='delete_poll_view'),
    path('poll/<int:pk>/create_choice/', ChoiceCreateView.as_view(), name='create_choice_view'),
    path('poll/<int:pk>/choice/update/', ChoiceUpdateView.as_view(), name='update_choice_view'),
    path('poll/<int:pk>/choice/delete/', ChoiceDeleteView.as_view(), name='delete_choice_view'),
    path('poll/<int:pk>/answer/', AnswerPollView.as_view(), name='poll_answer_view'),
    path('answers/list/', AnswersListView.as_view(), name='answers_list_view'),

]
