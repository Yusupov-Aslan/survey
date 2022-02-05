from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from survey.forms import PollForm
from survey.models import Poll


class AddPollView(CreateView):
    model = Poll
    form_class = PollForm
    template_name = "polls/create.html"

    def get_success_url(self):
        return reverse("detail_view", kwargs={"pk": self.object.pk})


class PollView(ListView):
    model = Poll
    context_object_name = 'polls'
    template_name = 'polls/view.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created_at')


class PollDetailView(DetailView):
    template_name = 'polls/detail_poll.html'
    model = Poll


class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'polls/update.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse("detail_view", kwargs={"pk": self.object.pk})


class PollDeleteView(DeleteView):
    model = Poll
    template_name = 'polls/delete.html'

    def get_success_url(self):
        return reverse("polls_view")


