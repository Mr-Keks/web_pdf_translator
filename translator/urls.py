from django.urls import path

from translator import views


urlpatterns = [
	path('', views.TranslatePage.as_view(), name="translate_page"),
    path('description/', views.DescriptionPage.as_view(), name="description_page"),
]