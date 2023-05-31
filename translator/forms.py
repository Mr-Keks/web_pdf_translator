from django import forms


class TranslateForm(forms.Form):
	input_field  = forms.CharField(widget=forms.Textarea(attrs={'id': 'originText'}))
	output_field = forms.CharField(required=False, widget=forms.Textarea(attrs={'id': 'translatedText'}))


class DropSpacesForm(forms.Form):
	input_field = forms.CharField(widget=forms.Textarea(attrs={'id': 'originText'}))