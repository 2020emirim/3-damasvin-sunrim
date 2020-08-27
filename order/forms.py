from django import forms

from order.models import Order


class OrderModelForm(forms.ModelForm):
    _CUPS = (('0', '레귤러'), ('1', '점보'))
    _ICES = (('0', '0%'), ('50', '50%'), ('100', '100%'), ('150', '150%'))
    _SUGARS = (('0', '0%'), ('50', '50%'), ('100', '100%'), ('150', '150%'))
    _PEALRS = (('타피오카', '타피오카'), ('코코', '코코'), ('젤리', '젤리'), ('알로에', '알로에'))
    cup = forms.ChoiceField(widget=forms.Select, choices=_CUPS, initial=0)
    ice = forms.ChoiceField(widget=forms.RadioSelect, choices=_ICES, initial=100)
    suger = forms.ChoiceField(widget=forms.RadioSelect, choices=_SUGARS, initial=100)
    pearl = forms.ChoiceField(widget=forms.RadioSelect, choices=_PEALRS, initial='타피오카')

    class Meta:
        model = Order
        fields = ['drink', 'cup', 'ice', 'suger', 'pearl', 'stock', 'price']