from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin


class HouseholdDashboard(EdcBaseViewMixin, TemplateView):

    template_name = 'analysis/household_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        forms = []
        context.update(
            members=[['Coulson Kgathi', 'Father'], ['Liam Kghathi', 'Son']],
            head_of_household=None,
            total_household_members=0,
            household_identifier='H99KEB7G',
            forms=forms)
        return context