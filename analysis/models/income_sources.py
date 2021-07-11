from django.db import models

from edc_base.model_mixins import BaseUuidModel
from django.db.models.deletion import PROTECT
from ..choices import CROPS, LIVESTOCK


class Income(BaseUuidModel):

    earn_income = models.IntegerField(
        verbose_name='How many household members earn income',
        null=True,
        blank=True,
        max_length=200)

    crop_name = models.CharField(
        verbose_name='Was your household engaged in any of the following '
                     'income generation activities during the last 12 months',
        null=True,
        choices=CROPS,
        blank=True,
        max_length=100)

    crop_name_other = models.CharField(
        verbose_name='Other specify',
        null=True,
        blank=True,
        max_length=200)

    livestock_name = models.CharField(
        verbose_name='Livestock Name',
        null=True,
        choices=LIVESTOCK,
        blank=True,
        max_length=100)

    livestock_name_other = models.CharField(
        verbose_name='Other ,Specify',
        null=True,
        blank=True,
        max_length=200)
