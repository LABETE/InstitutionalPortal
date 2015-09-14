from django import forms

from .models import Debt


class DebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        fields = ('username', 'year', 'semester', 'inscription_payment',
            'library_debts', 'laboratory_debts', )
