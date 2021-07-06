from django.db import models

from edc_base.model_mixins import BaseUuidModel
from django.db.models.deletion import PROTECT
from ..choices import LIVESTOCK, COUNT
from .agricultural_production import AgriculturalProduction


class AgriculturalLivestockProduction(BaseUuidModel):
    agric_production = models.ForeignKey(AgriculturalProduction,
                                   on_delete=PROTECT)

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

    livestock_no = models.CharField(
        verbose_name='How many livestock do you currently own?',
        null=True,
        blank=True,
        max_length=200)

    increased_decreased = models.CharField(
        verbose_name='If increased or decreased',
        null=True,
        blank=True,
        choices=COUNT,
        max_length=30)

    reason = models.CharField(
        verbose_name='State main reason for change',
        null=True,
        blank=True,
        max_length=40)
