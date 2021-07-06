from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import AgriculturalProduction


class AgriculturalProductionForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = AgriculturalProduction
        fields = '__all__'