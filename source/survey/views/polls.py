from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from survey.forms import PollForm, ChoiceForm
from survey.models import Poll, Choice, Answer


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

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['object'] = self.object
            choices = self.object.choices.all()
            context['choices'] = choices
            context['form'] = ChoiceForm()
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super().get_context_data(**context)


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


class ChoiceCreateView(CreateView):
    model = Choice
    template_name = "polls/detail_poll.html"
    form_class = ChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        return redirect('detail_view', pk=poll.pk)


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choices/choice_update.html'
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse("detail_view", kwargs={"pk": self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choices/delete.html'

    def get_success_url(self):
        return reverse("detail_view", kwargs={"pk": self.object.poll.pk})


class AnswerPollView(View):
    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        return render(request, "answers/answer.html", {"poll": poll})

    def post(self, request, *args, **kwargs ):
        choice_id = request.POST.get("answer")
        poll_id = self.kwargs.get('pk')
        Answer.objects.create(poll_id=poll_id, choice_id=choice_id)
        return redirect("answers_list_view")


class AnswersListView(ListView):
    model = Answer
    context_object_name = 'answers'
    template_name = 'answers/answers_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created_at')