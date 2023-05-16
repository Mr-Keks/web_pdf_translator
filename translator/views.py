from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView, TemplateView

from googletrans import Translator

import re

from translator import forms


class TranslatePage(FormView):
	'''
	Translate page view
	'''

	template_name = 'translate_page.html'
	http_method_names = ['get', 'post']
	form_class = forms.TranslateForm
	success_url = '/'

	def get(self, request, *args, **kwargs):
		return self.render_to_response(self.get_context_data())
	
	def post(self, request, *args, **kwargs):
		form = self.get_form()

		if form.is_valid():
			# delete all of 'enters'
			white_text = []
			input_field = form.cleaned_data['input_field']

			c = 0
			res = ['']
			for i in input_field.split('\n'):
				if i == '\r':
					c +=1
					res.append('')
					
				res[c] += i.strip() + ' '

			input_field = '\n'.join(res)
			# find all smile symbols and replace for '-'
			input_field = re.sub(chr(2), "", input_field)

			# translate text
			translator = Translator()
			output_field = translator.translate(input_field, dest='uk').text

			form = forms.TranslateForm(initial={'input_field':input_field, 'output_field':output_field})

			return render(request, 'translate_page.html', {"form": form})
		else:
			return self.form_invalid(form)
	
class DescriptionPage(TemplateView):
	'''
	View generate template with describing app features.
	'''
	
	template_name = 'describe_page.html'
	