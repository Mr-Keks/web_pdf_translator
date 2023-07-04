from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView, TemplateView

import re
import json

from translator import forms
from .utils import drop_spaces, translate_text


class TranslatePage(FormView):
	template_name = 'translate_page.html'
	form_class = forms.TranslateForm
	success_url = '/'

	def get_initial(self):
		return {'text_language': 'en', 'translate_language': 'uk'}

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['is_hide'] = True
		context['languages'] = self.load_languages()
		return context

	def load_languages(self):
		try:
			with open("staticfiles/data/languages.json", 'r') as f:
				languages = json.load(f)
			return languages
		except Exception as e:
			print("Error reading languages file:", e)
			return {}

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			input_field = form.cleaned_data['input_field']
			translate_language = form.cleaned_data['translate_language']

			cleaned_field = drop_spaces(input_field)
			text_language, translated_field = translate_text(cleaned_field, translate_lang=translate_language)
			
			form = forms.TranslateForm(initial={
				'input_field': cleaned_field,
				'output_field': translated_field,
				'text_language': text_language,
				'translate_language': translate_language
			})


			context = self.get_context_data(form=form)
			context['is_hide'] = False
			return self.render_to_response(context)
		else:
			errors = form.errors.as_data()
			for field, error_list in errors.items():
				for error in error_list:
					print(field, error.message)
			return super().form_invalid(form)

	
class DescriptionPage(TemplateView):
	'''
	View generate template with describing app features.
	'''
	
	template_name = 'describe_page.html'


class DropSpacesPage(FormView):
	template_name = "drop_spaces_page.html"
	http_method_names = ['get', 'post']
	form_class = forms.DropSpacesForm
	success_url = '/'

	def get(self, request: HttpRequest, *args: str, **kwargs: Any):
		kwargs["is_hide"] = True
		return self.render_to_response(self.get_context_data(**kwargs))
	
	def post(self, request, *args, **kwargs):
		form = self.get_form()
		
		if form.is_valid():
			form_text = form.cleaned_data['input_field']
			form = forms.DropSpacesForm(initial={'input_field': drop_spaces(form_text)})
			
			return self.render_to_response(self.get_context_data(form=form))
