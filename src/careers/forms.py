from django import forms

from .models import Career

class CareerForm(forms.ModelForm):
	class Meta:
		model = Career
		fields = [
			'code',
			'career',
			'study_plan',
		]