from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model_mixins import BaseUuidModel

from ..choices import GENDER, RELATIONSHIP, EDUCATION, YES_NO_NA, MARITAL_STATUS
from .household import Household



class HouseholdMember(BaseUuidModel):

    household = models.ForeignKey(Household, on_delete=PROTECT)

    id_number = models.CharField(
        verbose_name='ID Number',
        null=True,
        blank=True,
        max_length=100)

    full_name = models.CharField(
        verbose_name='Full name',
        null=True,
        blank=True,
        max_length=200)

    age_in_years = models.IntegerField(
        verbose_name='What is the participants age?',
        blank=True,
        null=True,
        help_text='(Years)', )
    
    gender = models.CharField(
        verbose_name='Gender',
        choices=GENDER,
        null=True,
        blank=True,
        max_length=1)

    relationship = models.CharField(
        verbose_name='Relationship (e.g son, daughter, mother, father, son-in-law)',
        choices=RELATIONSHIP,
        null=True,
        blank=True,
        max_length=100)
    
    education_level = models.CharField(
        verbose_name='Education Level',
        choices=EDUCATION,
        null=True,
        blank=True,
        max_length=8)

    school_attendance = models.CharField(
        verbose_name='Has been regularly attending school the past six months.',
        choices=YES_NO_NA,
        null=True,
        blank=True,
        max_length=10)

    marital_status = models.CharField(
        verbose_name='What is the marital status?',
        choices=MARITAL_STATUS,
        null=True,
        blank=True,
        max_length=50)
    

