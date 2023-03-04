from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from googletrans import Translator

import re

from translator import forms

def translate_page(request):
	if request.method == "GET":
		print('get')
		translate_form = forms.TranslateForm()
		return render(request, 'translate_page.html', {'form': translate_form})

	elif request.method == "POST":
		translate_form = forms.TranslateForm(request.POST)
		
		if translate_form.is_valid():
			# delete all of 'enters'
			white_text = []
			input_field = translate_form.cleaned_data['input_field']

			for word in input_field.split("\n"):
				white_text.append(word.rstrip())
			# text without enter`s
			input_field = " ".join(white_text)
			# find all smile symbols and replace for '-'
			input_field = re.sub(chr(2), "-", input_field)

			# translate text
			translator = Translator()
			output_field = translator.translate(input_field, dest='uk').text

			new_form = forms.TranslateForm(initial={'input_field':input_field, 'output_field':output_field})
			
			return render(request, 'translate_page.html', {"form": new_form})








