from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin

from ..models import FoodSecurityLivelihood

    
class FoodSecurityLivelihoodView(EdcBaseViewMixin, NavbarViewMixin, TemplateView):

    template_name = 'analysis/food_security_livelihood.html'
    navbar_name = 'analysis'
    navbar_selected_item = 'food_security'
    model_cls = FoodSecurityLivelihood

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        participants = FoodSecurityLivelihood.objects.all()
        context.update(
            participants=participants,
            participant_add_url=self.model_cls().get_absolute_url())
        return context  
