from django import forms
from .models import blogs
from djrichtextfield.widgets import RichTextWidget 

class blogform(forms.ModelForm):
	class Meta:
		model = blogs
		fields = [
		'title',
		'auther',
		'date',
		'article',
		'image'

		]
		widgets = {
        'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'article' : RichTextWidget()
    	}