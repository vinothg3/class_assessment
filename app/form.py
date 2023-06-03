from django import forms

from app.models import *

class user_form(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']

        widgets={'password':forms.PasswordInput()}

class question_form(forms.ModelForm):
    class Meta:
        model=Question
        fields=['question']
        widgets={'question':forms.Textarea()}
class answer_form(forms.ModelForm):
    class Meta:
        model=Allanswer
        fields=['answer','question']