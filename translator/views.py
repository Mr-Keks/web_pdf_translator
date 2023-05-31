from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView, TemplateView

import re

from translator import forms
from .utils import drop_spaces, translate_text


class TranslatePage(FormView):
	'''
	Translate page view
	'''

	template_name = 'translate_page.html'
	http_method_names = ['get', 'post']
	form_class = forms.TranslateForm
	success_url = '/'

	def get(self, request, *args, **kwargs):
		kwargs["is_hide"] = True
		return self.render_to_response(self.get_context_data(**kwargs))
	
	def post(self, request, *args, **kwargs):
		form = self.get_form()

		if form.is_valid():
			input_field = form.cleaned_data['input_field']
			cleaned_field = drop_spaces(input_field)
			translated_field = translate_text(cleaned_field)

			form = forms.TranslateForm(initial={'input_field':cleaned_field, 'output_field':translated_field})

			return render(request, 'translate_page.html', {"form": form, "is_hide": False})
		else:
			return self.form_invalid(form)
	
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
