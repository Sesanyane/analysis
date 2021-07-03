from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin

from ..models import RuralCommunityRapidAssessment


class VaccineAwarenessView(EdcBaseViewMixin, NavbarViewMixin, TemplateView):

    template_name = 'analysis/vaccine_awareness.html'
    navbar_name = 'analysis'
    navbar_selected_item = 'vaccine'
    model_cls = RuralCommunityRapidAssessment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        participants = RuralCommunityRapidAssessment.objects.all()
        context.update(
            participants=participants,
            participant_add_url=self.model_cls().get_absolute_url())
        return context
