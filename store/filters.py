import django_filters
from .models import Product, ProductFeature
from category.models import Brand, SubCategory
from django.db import models
from django import forms

class productFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label="Min", widget=forms.TextInput(attrs={'class': 'form-control'}))
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label="Max", widget=forms.TextInput(attrs={'class': 'form-control'}))
    type = django_filters.CharFilter(field_name='feature__type_of_control', lookup_expr='icontains', label="type", widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    brand = django_filters.ModelMultipleChoiceFilter(
        queryset=Brand.objects.all(),
        label='Brands',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-label'}),
    )


        



        