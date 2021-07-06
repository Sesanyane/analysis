from django.db import models

from edc_base.model_mixins import BaseUuidModel
from django.db.models.deletion import PROTECT
from ..choices import YES_NO, CROPS
from .agricultural_production import AgriculturalProduction


class AgriculturalCropProduction(BaseUuidModel):

    agric_production = models.ForeignKey(AgriculturalProduction,
                                         on_delete=PROTECT)

    crop_name = models.CharField(
        verbose_name='Crop Name',
        null=True,
        choices=CROPS,
        blank=True,
        max_length=100)

    hectares = models.CharField(
        verbose_name='How many hectares',
        null=True,
        blank=True,
        max_length=200)

    expected_harvest = models.CharField(
        verbose_name='How much do you expect to harvest?(KG)',
        null=True,
        blank=True,
        max_length=200)

    sell_crop = models.CharField(
        verbose_name='Do you intend to sell this crop',
        null=True,
        blank=True,
        choices=YES_NO,
        max_length=10)

    sell_crop_reason = models.CharField(
        verbose_name='Why do you intend to sell this crop (main reason)?',
        null=True,
        blank=True,
        max_length=50)

    storage = models.CharField(
        verbose_name='Do you have storage for this crop?',
        null=True,
        blank=True,
        choices=YES_NO,
        max_length=10)

    storage_type = models.CharField(
        verbose_name='What type of storage is this',
        null=True,
        blank=True,
        max_length=40)
