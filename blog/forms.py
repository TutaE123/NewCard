from django import forms
from .models import Denunc, Cart, Koloda

class DenuncForm(forms.ModelForm):

    class Meta:
        model = Denunc
        fields = ('title', 'offender', 'offenses', 'published_date', 'image',)


class KolodaForm(forms.ModelForm):

    class Meta:
        model = Koloda
        fields = ('title',)


class CartForm(forms.ModelForm):

    class Meta:
        model = Cart
        fields = ('koloda', 'лицо', 'изнанка')
