from edc_constants.constants import OTHER

from edc_list_data import PreloadData

list_data = {
    'analysis.learnvaccine': [
        ('tv', 'TV'),
        ('radio', 'Radio'),
        ('social_media', 'Social media (Facebook, Twitter, Instagram, WhatsApp)'),
        ('print_media', 'Print media (news papers)'),
        ('people', 'People'),
        ('health_worker', 'Health Worker'),
        ('redcross_volunteers', 'Botswana Red Cross Volunteers'),
        (OTHER, 'Other, Specify'),
    ],
    'analysis.role': [
        ('kgosi', 'Kgosi'),
        ('kgosana', 'Kgosana'),
        ('mp', 'Member of Parliament'),
        ('councillor', 'Councillor'),
        ('pastor', 'Pastor/Priest/Imam/Rabbi'),
        ('commitee_member', 'Member of Committee in the Village'),
        ('public_servant', 'Public Servant'),
        ('community_member', 'Community Member'),
        (OTHER, 'Other, Specify'),
    ],
}

preload_data = PreloadData(
    list_data=list_data)
