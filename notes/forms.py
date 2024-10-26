from .import models
from django import forms #type:ignore
from django.core.exceptions import ValidationError #type:ignore
class Notesform(forms.ModelForm):
    class Meta:
        model=models.Notes
        fields=['title','notes'] 
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control my-5'}),
            'notes':forms.Textarea(attrs={'class':'form-control mb-5'}),
        }
        label={
            'notes': 'Write your thoughts here: '
        }


    def clean_title(self):
        title=self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('we only accept notes about django!')
        return title