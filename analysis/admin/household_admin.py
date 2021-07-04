from django.contrib import admin

from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)

from ..admin_site import analysis_admin
from ..forms import HouseholdForm
from ..models import Household
from .household_member_admin import HouseholdMemberInlineAdmin



class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin,
                      ModelAdminRedirectOnDeleteMixin,
                      ModelAdminSiteMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'


@admin.register(Household, site=analysis_admin)
class HouseholdAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = HouseholdForm

    fieldsets = (
        (None, {
            'fields': (
                'household_identifier',
                'report_date',
                'district',
                'village',
                'kgotla',
                'plot_number',
                'household_type',
                'total_houshold_members',
                'interview_date',
                'enumerator_name',
                'enumerator_cell',
                'begin_interview',
            )}),)

    inlines = [HouseholdMemberInlineAdmin, ]
    
    radio_fields = {
                    'village': admin.VERTICAL,
                    'district': admin.VERTICAL,
                    'kgotla': admin.VERTICAL,
                    'household_type': admin.VERTICAL,
                    'begin_interview': admin.VERTICAL}

    list_display = ('household_identifier',
                'village',
                'district',)

    search_fields = ('household_identifier',)
