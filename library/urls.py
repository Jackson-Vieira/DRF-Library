from re import template
from django.urls import path
from . views import LivrosListView


urlpatterns = [
    path('library/admin/', LivrosListView.as_view(), name='library-admin')
]