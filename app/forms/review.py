from django import forms
from ..models import Review

class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Write Review"}))

    class Meta:
        model = Review
        fields = ['text', 'score']