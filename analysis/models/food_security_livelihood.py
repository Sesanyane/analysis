from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_search.model_mixins import SearchSlugManager
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_base.sites import SiteModelMixin

from ..choices import COMMUNITY, DISTRICT


from edc_identifier.subject_identifier import SubjectIdentifier


class SubjectIdentifier(SubjectIdentifier):

    template = '{protocol_number}-0{site_id}{device_id}{sequence}'


class FoodSecurityLivelihoodManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, subject_identifier):
        return self.get(subject_identifier=subject_identifier)


class FoodSecurityLivelihood(
        NonUniqueSubjectIdentifierModelMixin, SiteModelMixin,
        UpdatesOrCreatesRegistrationModelMixin, BaseUuidModel):

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50,
        null=True)

    report_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Report Date')

    community = models.CharField(
        verbose_name='Community',
        choices=COMMUNITY,
        null=True,
        blank=True,
        max_length=200)

    plot_number = models.CharField(
        verbose_name='Plot Number',
        null=True,
        blank=True,
        max_length=100)

    district = models.CharField(
        verbose_name='District',
        choices=DISTRICT,
        null=True,
        blank=True,
        max_length=200)

    objects = FoodSecurityLivelihoodManager()

    def __str__(self):
        return self.subject_identifier

    def make_new_identifier(self):
        """Returns a new and unique identifier.

        Override this if needed.
        """
        subject_identifier = SubjectIdentifier(
            identifier_type='subject',
            requesting_model=self._meta.label_lower,
            site=self.site)
        return subject_identifier.identifier

    def save(self, *args, **kwargs):
        if self.created and not self.subject_identifier:
            self.subject_identifier = self.update_subject_identifier_on_save()
        super().save(*args, **kwargs)
    
    class Meta:
        app_label = 'analysis'
        verbose_name = 'Food Security & Livelihood'
        verbose_name_plural = 'Food Security & Livelihood'
