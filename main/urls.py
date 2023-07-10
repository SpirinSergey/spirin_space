from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='main'),
    path('family_tree', FamilyTree.as_view(), name='family_tree'),
    path('about_me', AboutMe.as_view(), name='about_me'),
    path('memory_of_bygone_years', MemoryOfBygoneYears.as_view(), name='memory_of_bygone_years'),
    path('blog', Blog.as_view(), name='blog'),
    path('contact', Contact.as_view(), name='contact'),


]
