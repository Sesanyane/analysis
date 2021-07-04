from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_search.model_mixins import SearchSlugManager
from edc_base.sites import SiteModelMixin

from ..choices import COMMUNITY, DISTRICT, HOUSEHOLD_TYPE, YES_NO

from ..identifiers import HouseholdIdentifier


class HouseholdManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, household_identifier):
        return self.get(household_identifier=household_identifier)


class Household(SiteModelMixin, BaseUuidModel):

    identifier_cls = HouseholdIdentifier

    household_identifier = models.CharField(
        verbose_name='Household Identifier',
        max_length=25,
        unique=True,
        editable=False)

    report_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Report Date')

    district = models.CharField(
        verbose_name='District',
        choices=DISTRICT,
        null=True,
        blank=True,
        max_length=200)

    village = models.CharField(
        verbose_name='Village',
        choices=COMMUNITY,
        null=True,
        blank=True,
        max_length=200)

    kgotla = models.CharField(
        verbose_name='Kgotla',
        choices=COMMUNITY,
        null=True,
        blank=True,
        max_length=200)

    plot_number = models.CharField(
        verbose_name='Plot Number',
        null=True,
        blank=True,
        max_length=100)

    household_type = models.CharField(
        verbose_name='Household type',
        choices=HOUSEHOLD_TYPE,
        null=True,
        blank=True,
        max_length=200)

    total_houshold_members = models.IntegerField(
        verbose_name='Total number of persons who live in the household',
        null=True,
        blank=True,)

    interview_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Date of Interview')

    enumerator_name = models.CharField(
        verbose_name='Enumerator \'s name',
        null=True,
        blank=True,
        max_length=200)

    enumerator_cell = models.CharField(
        verbose_name='Enumerator cell number',
        null=True,
        blank=True,
        max_length=200)

    begin_interview = models.CharField(
        verbose_name='Do you want to begin the interview?',
        null=True,
        blank=True,
        choices=YES_NO,
        max_length=10)
    

    objects = HouseholdManager()

    def __str__(self):
        return self.household_identifier

    def save(self, *args, **kwargs):
        if not self.household_identifier:
            self.household_identifier = self.identifier_cls().identifier
        super().save(*args, **kwargs)
    
    class Meta:
        app_label = 'analysis'
        verbose_name = 'Household'
        verbose_name_plural = 'Household'
