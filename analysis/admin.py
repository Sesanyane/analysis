from django.contrib import admin

from .models import RuralCommunityRapidAssessment
from .forms import RuralCommunityRapidAssessmentForm


@admin.register(RuralCommunityRapidAssessment)
class RuralCommunityRapidAssessmentAdmin(admin.ModelAdmin):

    form = RuralCommunityRapidAssessmentForm

    fieldsets = (
        (None, {
            'fields': (
                'community',
                'plot_number',
                'district',
                'full_name',
                'gender',
                'age_in_years',
                'contracts',
                'role',
                'role_other',
                'covid19_awareness',
                'covid19_learning',
                'covid19_learning_other',
                'vaccine_assess',
                'vaccine_assess_reason',
                'vaccine_assess_challanges',
                'va_challanges_other',
                'vaccine_trust',
                'vaccine_trust_other',
                'vaccine_recommendation',
                'vaccine_recommendation_other',
                'vaccination_importance',
                'vaccine_reco_others',
                'vaccine_recom_other',
                'vaccine_reco_someone',
                'vaccine_reco_someone_other',
            )}),)
    
    radio_fields = {'gender': admin.VERTICAL,
                    'role': admin.VERTICAL,
                    'covid19_awareness': admin.VERTICAL,
                    'covid19_learning': admin.VERTICAL,
                    'vaccine_assess': admin.VERTICAL,
                    'vaccine_assess_challanges': admin.VERTICAL,
                    'vaccine_trust': admin.VERTICAL,
                    'vaccine_recommendation': admin.VERTICAL,
                    'vaccination_importance': admin.VERTICAL,
                    'vaccine_reco_others': admin.VERTICAL,
                    'vaccine_reco_someone': admin.VERTICAL,}
