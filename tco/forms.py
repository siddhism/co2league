from django import forms
from .models import *

class QuestionsForm(forms.ModelForm):
	class Meta:
		model = Questions
		fields = '__all__'

class Travel_questionsForm(forms.ModelForm):
	class Meta:
		model = Travel_questions
		fields = '__all__'

class Housing_questionsForm(forms.ModelForm):
	class Meta:
		model = Housing_questions
		fields = '__all__'		

class Food_questionsForm(forms.ModelForm):
	class Meta:
		model = Food_questions
		fields = '__all__'

class Shopping_questionsForm(forms.ModelForm):
	class Meta:
		model = Shopping_questions
		fields = '__all__'