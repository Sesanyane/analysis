from django.db import models

from edc_base.model_mixins import BaseUuidModel
from django.db.models.deletion import PROTECT
from ..choices import DURABLE_GOODS, SOCIAL_EVENTS, PERSONAl_OBJECTS, SERVICES, AGRICULTURAL_EXPENDITURE


class NonFoodExpenditure(BaseUuidModel):
    expenditure_items = models.CharField(
        verbose_name='Did household have any expenses on any item below over '
                     'the past 6 months',
        null=True,
        choices=DURABLE_GOODS,
        blank=True,
        max_length=100)

    amount_spent = models.DecimalField(
        verbose_name='What amount was spent by the household over the past 6 '
                     'months?',
        null=True,
        blank=True,
        max_length=50)

    social_events = models.CharField(
        verbose_name='Did household have any expenses on any item below over '
                     'the past 6 months',
        null=True,
        choices=SOCIAL_EVENTS,
        blank=True,
        max_length=100)

    amount_social_events = models.DecimalField(
        verbose_name='What amount was spent by the household over the past 6 '
                     'months?',
        null=True,
        blank=True,
        max_length=50)

    personal_objects = models.CharField(
        verbose_name='Did household have any expenses on any item below over '
                     'the past 6 months',
        null=True,
        choices=PERSONAl_OBJECTS,
        blank=True,
        max_length=100)

    amount_personal_objects = models.DecimalField(
        verbose_name='What amount was spent by the household over the past 6 '
                     'months?',
        null=True,
        blank=True,
        max_length=50)

    services = models.CharField(
        verbose_name='Did household have any expenses on any item below over '
                     'the past 6 months',
        null=True,
        choices=SERVICES,
        blank=True,
        max_length=100)

    amount_services = models.DecimalField(
        verbose_name='What amount was spent by the household over the past 6 '
                     'months?',
        null=True,
        blank=True,
        max_length=50)

    agric_expense = models.CharField(
        verbose_name='Did household have any expenses on any item below over '
                     'the past 6 months',
        null=True,
        choices=AGRICULTURAL_EXPENDITURE,
        blank=True,
        max_length=100)

    amount_agric_expense = models.DecimalField(
        verbose_name='What amount was spent by the household over the past 6 '
                     'months?',
        null=True,
        blank=True,
        max_length=50)
