from django.shortcuts import render
from django.http import HttpResponse        # from the django.http module import the HttpResponse class
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"
