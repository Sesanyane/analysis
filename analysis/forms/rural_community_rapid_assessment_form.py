from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import RuralCommunityRapidAssessment



class RuralCommunityRapidAssessmentForm(SiteModelFormMixin, forms.ModelForm):
    
    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False)

    class Meta:
        model = RuralCommunityRapidAssessment
        fields = '__all__'