from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import AgriculturalCropProduction


class AgriculturalCropProductionForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = AgriculturalCropProduction
        fields = '__all__'