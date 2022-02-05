from django import forms

from survey.models import Poll


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ("question", )
