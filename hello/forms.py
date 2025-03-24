from django import forms
from hello.models import LogMessage, AttackProfile

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required

class LogAttackProfilesForm(forms.ModelForm):
	class Meta:
		model = AttackProfile
		fields = ("attacks",)   # NOTE: the trailing comma is required