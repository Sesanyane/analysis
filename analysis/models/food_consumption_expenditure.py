from django.db import models

from edc_base.model_mixins import BaseUuidModel
from django.db.models.deletion import PROTECT
from ..choices import YES_NO, FOOD_CATEGORIES, DAYS


class FoodConsumptionExpenditure(BaseUuidModel):

    food_categories = models.CharField(
        verbose_name='In the last 7 days did anyone in household consume the '
                     'below food',
        null=True,
        choices=FOOD_CATEGORIES,
        blank=True,
        max_length=100)

    days = models.CharField(
        verbose_name='In the last 7 how many days did you consume the '
                     'food',
        choices=DAYS,
        null=True,
        blank=True,
        max_length=50)

    source_food = models.CharField(
        verbose_name='What was the main source of this food',
        null=True,
        blank=True,
        max_length=200)

    cost = models.DecimalField(
        verbose_name='How much did it cost',
        null=True,
        blank=True,)

    estimate_cost = models.CharField(
        verbose_name='Estimate cost of all food the household did not buy',
        null=True,
        blank=True,
        max_length=50)