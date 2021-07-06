from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import AgriculturalLivestockProduction


class AgriculturalLivestockProductionForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = AgriculturalLivestockProduction
        fields = '__all__'