from django.urls import path

from translator import views


urlpatterns = [
	path('', views.translate_page, name="translate_page"),
]