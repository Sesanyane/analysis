from django.contrib import admin
from edc_model_admin import  TabularInlineMixin

from ..models import HouseholdMember
from ..forms import HouseholdMemberForm


class HouseholdMemberInlineAdmin(TabularInlineMixin,
                            admin.TabularInline):
    model = HouseholdMember
    form = HouseholdMemberForm
    extra = 0

    fieldsets = (
        (None, {
            'fields': [
                'food_security_livelihood',
                'id_number',
                'full_name',
                'age_in_years',
                'gender',
                'relationship',
                'education_level',
                'school_attendance',
                'marital_status']}
         ),)

    def has_change_permission(self, request, obj):
        if obj:
            return request.user.username == obj.user_created
        else:
            return True

    def has_add_permission(self, request, obj):
        if obj:
            return request.user.username == obj.user_created
        else:
            return True