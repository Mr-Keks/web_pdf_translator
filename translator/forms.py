from django import forms


class TranslateForm(forms.Form):
	input_field  = forms.CharField(widget=forms.Textarea(attrs={'id': 'originText'}), max_length=5000)
	output_field = forms.CharField(required=False, widget=forms.Textarea(attrs={'id': 'translatedText'}))
	text_language = forms.CharField(required=False)
	translate_language = forms.CharField(required=False)

class DropSpacesForm(forms.Form):
	input_field = forms.CharField(widget=forms.Textarea(attrs={'id': 'originText'}))