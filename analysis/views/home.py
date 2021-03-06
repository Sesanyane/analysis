from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin

from edc_base.view_mixins import AdministrationViewMixin



class AdministrationView(EdcBaseViewMixin, NavbarViewMixin,
                         AdministrationViewMixin, TemplateView):

    navbar_name = 'analysis'
    navbar_selected_item = 'administration'



class HomeView(EdcBaseViewMixin, NavbarViewMixin, TemplateView):

    template_name = 'analysis/home.html'
    navbar_name = 'analysis'
    navbar_selected_item = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update()
        return context
