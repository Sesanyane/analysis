from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model_mixins import BaseUuidModel

from ..choices import (
    ROOF_MATERIAL, FLOOR_MATERIAL, WALL_MATERIAL,
    SANITARY_FACILITY, DRINKING_WATER, LIGHTING,
    COOKING_ENERGY, YES_NO, HOUSE_ARRANGEMENT, WASTE_DISPOSAL)
from .household import Household
from .list_models import Assets



class HousingCharacteristics(BaseUuidModel):

    household = models.ForeignKey(Household, on_delete=PROTECT)

    roof_material = models.CharField(
        verbose_name='What is the main construction materials used to build the roof of the house?',
        null=True,
        blank=True,
        choices=ROOF_MATERIAL,
        max_length=150)

    floor_material = models.CharField(
        verbose_name='What was the main construction material used to build the floor of the house?',
        null=True,
        blank=True,
        choices=FLOOR_MATERIAL,
        max_length=150)

    wall_material = models.CharField(
        verbose_name='What was the main construction material used to build the exterior walls of the house?',
        null=True,
        blank=True,
        choices=WALL_MATERIAL,
        max_length=150)

    occupied_rooms = models.IntegerField(
        verbose_name='How many separate rooms do the member of this household occupy?',
        blank=True,
        null=True,
        help_text='(Do not count bathrooms, toilets, storerooms, or garage)', )
    
    sanitary_facility = models.CharField(
        verbose_name='What is the main type of sanitary facility used by the household?',
        choices=SANITARY_FACILITY,
        null=True,
        blank=True,
        max_length=100)

    drinking_water = models.CharField(
        verbose_name='What is the main source of drinking water for the household?',
        choices=DRINKING_WATER,
        null=True,
        blank=True,
        max_length=100)
    
    water_source_distance = models.DecimalField(
        verbose_name='What is the distance from your house to the source of water you most commonly use for drinking water this season?',
        blank=True,
        null=True,
        help_text='(Kilometers)', )

    lighting = models.CharField(
        verbose_name='What is the main source of lighting for the main building of the household?',
        choices=LIGHTING,
        null=True,
        blank=True,
        max_length=100)

    lighting_other = models.CharField(
        verbose_name='If other on the lighting question above specify',
        null=True,
        blank=True,
        max_length=100)

    cooking_energy = models.CharField(
        verbose_name='What is the main source of energy used to cook meals for the household?',
        choices=COOKING_ENERGY,
        null=True,
        blank=True,
        max_length=100)

    cooking_energy_other = models.CharField(
        verbose_name='If other on the cooking energy source question above specify',
        null=True,
        blank=True,
        max_length=100)

    house_ownership = models.CharField(
        verbose_name='Does anyone in your household own this house?',
        choices=YES_NO,
        null=True,
        blank=True,
        max_length=100)

    house_arangement = models.CharField(
        verbose_name='What is the housing arrangement for this household?',
        choices=HOUSE_ARRANGEMENT,
        null=True,
        blank=True,
        max_length=100)

    house_arangement_other = models.CharField(
        verbose_name='If other on the housing arrangement question above specify',
        null=True,
        blank=True,
        max_length=100)

    waste_disposal = models.CharField(
        verbose_name='How does your household dispose of household waste?',
        choices=WASTE_DISPOSAL,
        null=True,
        blank=True,
        max_length=100)

    assets = models.ManyToManyField(
        Assets,
        verbose_name='Does any member of the household have any of the assets below?',
        blank=True,
        max_length=100)

    working_assets = models.ManyToManyField(
        Assets,
        verbose_name='Which of the assets owned by your household still works?',
        blank=True,
        max_length=100)


    class Meta:
        app_label = 'analysis'
        verbose_name = 'Housing Characteristics'
        verbose_name_plural = 'Housing Characteristics'
