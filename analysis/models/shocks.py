from django.db import models

from edc_base.model_mixins import BaseUuidModel
from django.db.models.deletion import PROTECT
from ..choices import LIVESTOCK, COUNT
from .agricultural_production import AgriculturalProduction


class Shocks(BaseUuidModel):

    shocks_household = models.CharField(
        verbose_name='What have been the main shocks that your household '
                     'experienced in the past 6 months?',
        null=True,
        blank=True,
        max_length=40)

    first = models.CharField(
        verbose_name='First',
        null=True,
        blank=True,
        max_length=200)

    second = models.CharField(
        verbose_name='Second',
        null=True,
        blank=True,
        max_length=200)

    third = models.CharField(
        verbose_name='Third',
        null=True,
        blank=True,
        max_length=30)

    prevention = models.CharField(
        verbose_name='How would you mainly prevent these from affecting you '
                     'in the future',
        null=True,
        blank=True,
        max_length=40)

    first_prevention = models.CharField(
        verbose_name='First',
        null=True,
        blank=True,
        max_length=200)

    second_prevention = models.CharField(
        verbose_name='Second',
        null=True,
        blank=True,
        max_length=200)

    third_prevention = models.CharField(
        verbose_name='Third',
        null=True,
        blank=True,
        max_length=30)

    rain_this_season = models.CharField(
        verbose_name='According to your experience how was the rain this '
                     'season compared to a normal year ',
        null=True,
        blank=True,
        max_length=40)