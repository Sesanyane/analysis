from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import HouseholdMember


class HouseholdMemberForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = HouseholdMember
        fields = '__all__'
