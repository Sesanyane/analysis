from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Household


class HouseholdForm(SiteModelFormMixin, forms.ModelForm):
    
    household_identifier = forms.CharField(
        label='Household Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False)

    class Meta:
        model = Household
        fields = '__all__'
