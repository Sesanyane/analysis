from django import forms

from .models import RuralCommunityRapidAssessment


class RuralCommunityRapidAssessmentForm(forms.ModelForm):
    
    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False)

    class Meta:
        model = RuralCommunityRapidAssessment
        fields = '__all__'
