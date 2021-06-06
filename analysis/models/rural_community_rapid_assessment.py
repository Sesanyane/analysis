from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_search.model_mixins import SearchSlugManager
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_base.sites import SiteModelMixin

from ..choices import (
    COMMUNITY, DISTRICT, GENDER, ROLE, YES_NO, MEDIA, VACCINE_ACCESS,
    VACCINE_TRUST, YES_NO_NOT_SURE, VACCINE_IMPORTANCE)


from edc_identifier.subject_identifier import SubjectIdentifier


class SubjectIdentifier(SubjectIdentifier):

    template = '{protocol_number}-0{site_id}{device_id}{sequence}'


class RuralCommunityRapidAssessmentManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, subject_identifier):
        return self.get(subject_identifier=subject_identifier)


class RuralCommunityRapidAssessment(
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
    
    full_name = models.CharField(
        verbose_name='Full name',
        null=True,
        blank=True,
        max_length=200)

    gender = models.CharField(
        verbose_name='Gender',
        choices=GENDER,
        null=True,
        blank=True,
        max_length=1)

    age_in_years = models.IntegerField(
        verbose_name='What is the participants age?',
        blank=True,
        null=True,
        help_text='(Years)', )

    contracts = models.CharField(
        verbose_name='Contacts',
        null=True,
        blank=True,
        max_length=100)

    role = models.CharField(
        verbose_name='What is your current role?',
        choices=ROLE,
        null=True,
        blank=True,
        max_length=200)

    role_other = models.CharField(
        verbose_name='If the answer to role above is other specify',
        null=True,
        blank=True,
        max_length=200)

    covid19_awareness = models.CharField(
        verbose_name='Are you aware of Coronavirus/COVID-19 Vaccine?',
        null=True,
        blank=True,
        choices=YES_NO,
        max_length=10)

    covid19_learning = models.CharField(
        verbose_name='If yes, where did you learn about Coronavirus/COVID-19 Vaccine?',
        null=True,
        blank=True,
        choices=MEDIA,
        max_length=100)

    covid19_learning_other = models.CharField(
        verbose_name='If the answer to where you learnt about COVID-19 above is other specify',
        null=True,
        blank=True,
        max_length=200)

    vaccine_assess = models.CharField(
        verbose_name='How easy is it to get vaccination service for yourself?',
        null=True,
        blank=True,
        choices=VACCINE_ACCESS,
        max_length=100)

    vaccine_assess_reason = models.CharField(
        verbose_name='If not easy what are the reasons?',
        null=True,
        blank=True,
        max_length=200)

    vaccine_assess_challanges = models.CharField(
        verbose_name='Is there anything that may stop you from getting the COVID-19 vaccine injection?',
        null=True,
        blank=True,
        choices=YES_NO,
        max_length=100)

    va_challanges_other = models.CharField(
        verbose_name='If the answer to things that may stop you from getting the vaccine is yes specify reasons',
        null=True,
        blank=True,
        max_length=200)

    vaccine_trust = models.CharField(
        verbose_name='How much would you trust the new COVID-19 vaccine if it was available for you?',
        null=True,
        blank=True,
        choices=VACCINE_TRUST,
        max_length=100)

    vaccine_trust_other = models.CharField(
        verbose_name='If you do not trust the vaccine state reasons why',
        null=True,
        blank=True,
        max_length=200)

    vaccine_recommendation = models.CharField(
        verbose_name='If the new COVID-19 vaccine is recommended for you, would you take it?',
        null=True,
        blank=True,
        choices=YES_NO_NOT_SURE,
        max_length=100)

    vaccine_recommendation_other = models.CharField(
        verbose_name='If you No or Not sure, why',
        null=True,
        blank=True,
        max_length=200)

    vaccination_importance = models.CharField(
        verbose_name='How important is it to get vaccine?',
        null=True,
        blank=True,
        choices=VACCINE_IMPORTANCE,
        max_length=100)

    vaccine_reco_others = models.CharField(
        verbose_name='Would you recommend COVID-19 vaccine to your community followers?',
        null=True,
        blank=True,
        choices=YES_NO_NOT_SURE,
        max_length=100)
    
    vaccine_recom_other = models.CharField(
        verbose_name='If you No or Not sure, why',
        null=True,
        blank=True,
        max_length=200)

    vaccine_reco_someone = models.CharField(
        verbose_name='Would you recommend the COVID-19 vaccine to someone?',
        null=True,
        blank=True,
        choices=YES_NO,
        max_length=100)

    vaccine_reco_someone_other = models.CharField(
        verbose_name='If No give reasons',
        null=True,
        blank=True,
        max_length=200)

    objects = RuralCommunityRapidAssessmentManager()

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
        verbose_name = 'Rural Community Rapid Assessment'
        verbose_name_plural = 'Rural Community Rapid Assessment'