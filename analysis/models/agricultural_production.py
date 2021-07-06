from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model_mixins import BaseUuidModel

from ..choices import WATERING


class AgriculturalProduction(BaseUuidModel):


    area_owned = models.CharField(
        verbose_name='What is the total land area owned by household?',
        null=True,
        blank=True,
        max_length=50,
        help_text='Hectare')

    area_cultivated = models.CharField(
        verbose_name='What is the total land area cultivated this season?',
        null=True,
        blank=True,
        max_length=50,
        help_text='Hectare')

    area_rented = models.CharField(
        verbose_name='What is the total land area rented?',
        null=True,
        blank=True,
        max_length=50,
        help_text='Hectare')

    method_watering = models.CharField(
        verbose_name='How do you water your crops',
        choices=WATERING,
        null=True,
        blank=True,
        max_length=10)
