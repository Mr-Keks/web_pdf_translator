from django.urls import path

from translator import views


urlpatterns = [
	path('', views.translate_page.as_view(), name="translate_page"),
]