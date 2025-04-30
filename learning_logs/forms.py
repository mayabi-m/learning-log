from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """A form for adding new topics."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.TextInput(attrs={'placeholder': 'Enter a new topic'})}
class EntryForm(forms.ModelForm):
    """A form for adding new entries."""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'placeholder': 'Enter your entry here'})}        