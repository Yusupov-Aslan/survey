from django import forms

from survey.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ("question",)


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('option_text',)
        widgets = {
            'option_text': forms.Textarea(attrs={'rows': 1, 'cols': 35}, )
        }
