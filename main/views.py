from django.views.generic import TemplateView

from .models import *


class Home(TemplateView):
    template_name = "main/pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Home'
        context["url"] = ''
        return context


class AboutMe(TemplateView):
    template_name = "main/pages/about_me.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Обо мне'
        context["url"] = ''
        return context


class FamilyTree(TemplateView):
    template_name = "main/pages/family_tree.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Family Tree'
        context["url"] = ''
        return context


class MemoryOfBygoneYears(TemplateView):
    template_name = "main/pages/memory_of_bygone_years.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Memory Of Bygone Years'
        context["url"] = ''
        return context


class Blog(TemplateView):
    template_name = "main/pages/blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Блог'
        context["url"] = ''
        return context


class Contact(TemplateView):
    template_name = "main/pages/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Contact'
        context["url"] = ''
        return context
