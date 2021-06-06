from django.db import models

GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)

ROLE = (
    ('kgosi', 'Kgosi'),
    ('kgosana', 'Kgosana'),
    ('mp', 'Member of Parliament'),
    ('councillor', 'Councillor'),
    ('pastor', 'Pastor/Priest/Imam/Rabbi'),
    ('commitee_member', 'Member of Committee in the Village'),
    ('public_servant', 'Public Servant'),
    ('community_member', 'Community Member'),
    ('other', 'Other')
)

YES_NO = (
    ('y', 'Yes'),
    ('n', 'No')
)

MEDIA = (
    ('tv', 'TV'),
    ('radio', 'Radio'),
    ('social_media', 'Social media (Facebook, Twitter, Instagram, WhatsApp)'),
    ('print_media', 'Print media (news papers)'),
    ('people', 'People'),
    ('health_worker', 'Health Worker'),
    ('redcross_volunteers', 'Botswana Red Cross Volunteers'),
    ('other', 'Other')
)

VACCINE_ACCESS = (
    ('not_easy', 'Not easy'),
    ('moderately_easy', 'Moderately easy'),
    ('extremely_easy', 'Extremely easy')
)

VACCINE_TRUST = (
    ('not_at_all', 'Not at all'),
    ('moderately', 'Moderately'),
    ('very_much', 'Very much')
)

YES_NO_NOT_SURE = (
    ('y', 'Yes'),
    ('n', 'No'),
    ('not_sure', 'Not sure')
)

VACCINE_IMPORTANCE = (
    ('very_important', 'Very Important'),
    ('important', 'Important'),
    ('not_important', 'Not important'),
    ('not_important_at_all', 'Not important at all')
)


class RuralCommunityRapidAssessment(models.Model):

    report_date = models.DateField('Report Date')

    community = models.CharField(
        verbose_name='Community',
        null=True,
        max_length=200)

    plot_number = models.CharField(
        verbose_name='Plot Number',
        null=True,
        max_length=100)

    district = models.CharField(
        verbose_name='District',
        null=True,
        max_length=200)
    
    full_name = models.CharField(
        verbose_name='Full name',
        null=True,
        max_length=200)

    gender = models.CharField(
        verbose_name='Gender',
        choices=GENDER,
        null=True,
        max_length=1)

    age_in_years = models.IntegerField(
        verbose_name='What is the participants age?',
        help_text='(Years)', )

    contracts = models.CharField(
        verbose_name='Contacts',
        null=True,
        max_length=100)

    role = models.CharField(
        verbose_name='What is your current role?',
        choices=ROLE,
        null=True,
        max_length=200)

    role_other = models.CharField(
        verbose_name='If the answer to role above is other specify',
        null=True,
        max_length=200)

    covid19_awareness = models.CharField(
        verbose_name='Are you aware of Coronavirus/COVID-19 Vaccine?',
        null=True,
        choices=YES_NO,
        max_length=10)

    covid19_learning = models.CharField(
        verbose_name='If yes, where did you learn about Coronavirus/COVID-19 Vaccine?',
        null=True,
        choices=MEDIA,
        max_length=100)

    covid19_learning_other = models.CharField(
        verbose_name='If the answer to where you learnt about COVID-19 above is other specify',
        null=True,
        max_length=200)

    vaccine_assess = models.CharField(
        verbose_name='How easy is it to get vaccination service for yourself?',
        null=True,
        choices=VACCINE_ACCESS,
        max_length=100)

    vaccine_assess_reason = models.CharField(
        verbose_name='If not easy what are the reasons?',
        null=True,
        max_length=200)

    vaccine_assess_challanges = models.CharField(
        verbose_name='Is there anything that may stop you from getting the COVID-19 vaccine injection?',
        null=True,
        choices=YES_NO,
        max_length=100)

    va_challanges_other = models.CharField(
        verbose_name='If the answer to things that may stop you from getting the vaccine is yes specify reasons',
        null=True,
        max_length=200)

    vaccine_trust = models.CharField(
        verbose_name='How much would you trust the new COVID-19 vaccine if it was available for you?',
        null=True,
        choices=VACCINE_TRUST,
        max_length=100)

    vaccine_trust_other = models.CharField(
        verbose_name='If you do not trust the vaccine state reasons why',
        null=True,
        max_length=200)

    vaccine_recommendation = models.CharField(
        verbose_name='If the new COVID-19 vaccine is recommended for you, would you take it?',
        null=True,
        choices=YES_NO_NOT_SURE,
        max_length=100)

    vaccine_recommendation_other = models.CharField(
        verbose_name='If you No or Not sure, why',
        null=True,
        max_length=200)

    vaccination_importance = models.CharField(
        verbose_name='How important is it to get vaccine?',
        null=True,
        choices=VACCINE_IMPORTANCE,
        max_length=100)

    vaccine_reco_others = models.CharField(
        verbose_name='Would you recommend COVID-19 vaccine to your community followers?',
        null=True,
        choices=YES_NO_NOT_SURE,
        max_length=100)
    
    vaccine_recom_other = models.CharField(
        verbose_name='If you No or Not sure, why',
        null=True,
        max_length=200)

    vaccine_reco_someone = models.CharField(
        verbose_name='Would you recommend the COVID-19 vaccine to someone?',
        null=True,
        choices=YES_NO,
        max_length=100)

    vaccine_reco_someone_other = models.CharField(
        verbose_name='If No give reasons',
        null=True,
        max_length=200)
