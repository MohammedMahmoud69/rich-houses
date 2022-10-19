from tkinter import Widget
import django_filters
from django import forms
from .models import Product

class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category']
