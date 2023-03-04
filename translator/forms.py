from django import forms


class TranslateForm(forms.Form):
	input_field  = forms.CharField(widget=forms.Textarea())
	output_field = forms.CharField(required=False, widget=forms.Textarea())
