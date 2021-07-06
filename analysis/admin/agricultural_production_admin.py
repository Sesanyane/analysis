from django.contrib import admin
from edc_model_admin import TabularInlineMixin
from edc_model_admin import audit_fieldset_tuple
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from ..admin_site import analysis_admin
from edc_base.sites.admin import ModelAdminSiteMixin
from ..forms import AgriculturalProductionForm, AgriculturalCropProductionForm, \
    AgriculturalLivestockProductionForm
from ..models import AgriculturalProduction, AgriculturalCropProduction, \
    AgriculturalLivestockProduction
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)


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


class AgriculturalCropProductionInlineAdmin(TabularInlineMixin,
                                            admin.TabularInline):
    model = AgriculturalCropProduction
    form = AgriculturalCropProductionForm
    extra = 0

    fieldsets = (
        (None, {
            'fields': [
                'crop_name',
                'hectares',
                'sell_crop',
                'sell_crop_reason',
                'storage',
                'storage_type']}
         ),)


class AgriculturalLivestockProductionInlineAdmin(TabularInlineMixin,
                                                 admin.TabularInline):
    model = AgriculturalLivestockProduction
    form = AgriculturalLivestockProductionForm
    extra = 0

    fieldsets = (
        (None, {
            'fields': [
                'livestock_name',
                'livestock_name_other',
                'livestock_no',
                'increased_decreased',
                'reason']}
         ),)


@admin.register(AgriculturalProduction, site=analysis_admin)
class AgriculturalProductionAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = AgriculturalProductionForm

    inlines = [AgriculturalCropProductionInlineAdmin,
               AgriculturalLivestockProductionInlineAdmin]

    fieldsets = (
        (None, {
            'fields': ('area_owned',
                       'area_cultivated',
                       'area_rented',
                       'method_watering',),
        }), audit_fieldset_tuple)

    radio_fields = {'method_watering': admin.VERTICAL, }
