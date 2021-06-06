from django import forms

from .models import RuralCommunityRapidAssessment


class RuralCommunityRapidAssessmentForm(forms.ModelForm):

    class Meta:
        model = RuralCommunityRapidAssessment
        fields = '__all__'
