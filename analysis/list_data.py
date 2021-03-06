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
    'analysis.assets': [
        ('radio', 'Radio'),
        ('tv', 'TV'),
        ('cell_phone', 'Cell phone'),
        ('video_dvd_vcr', 'Video/DVD/VCR'),
        ('satellite_dish_dstv_decoder', 'Satellite dish/DSTV decoder'),
        ('watch_clock', 'Watch/clock'),
        ('bed', 'Bed'),
        ('mattress', 'Mattress'),
        ('table', 'Table'),
        ('bench_or_chair', 'Bench or chair'),
        ('plot', 'Plot'),
        ('cabinet_cupboard_drawers_or_bureau', 'Cabinet, cupboard, drawers, or bueau'),
        ('solar_panel', 'Solar panel'),
        ('solar_lamps', 'Solar lamps'),
        ('kerosene_lamp', 'Kerosene lamp'),
        ('jewelry', 'Jewelry'),
        ('generator_set', 'Generator set'),
        ('energy_saving_stove', 'Energy saving stove'),
        ('sewing_machine', 'Sewing machine'),
        ('brick_molds', 'Brick molds'),
        ('small_kiosk_semausu', 'Small kiosk (semausu)'),
        ('donkey_cart', 'Donkey cart'),
        ('shovel', 'Shovel'),
        ('normal_plough', 'Normal plough'),
        ('disc_plough', 'Disc plough'),
        ('wheelbarrow', 'Wheelbarrow'),
        ('sickle', 'Sickle'),
        ('hoe', 'Hoe'),
        ('axe', 'Axe'),
        ('watering_can', 'Watering Can'),
        ('threshing_machine', 'Threshing machine'),
        ('groundnut_sheller', 'Groundnut sheller'),
        ('maize_mill', 'Maize mill'),
        ('water_mill', 'Water mill'),
        ('water_pump', 'Water pump'),
        ('oil_press_machine', 'Oil press machine'),
        ('cultivator', 'Cultivator'),
        ('harrow', 'Harrow'),
        ('planters', 'Planters'),
        ('sprayer', 'Sprayer'),
        ('treadle_pump', 'Treadle pump'),
        ('jab_planter', 'Jab planter'),
        ('direct_seeder_planter', 'Direct seeder planter'),
        ('ox_ddrawn_chains', 'Ox drawn chains'),
        ('small_tractors', 'Small tractors'),
        ('ridger_weeder', 'Ridger weeder'),
        ('slasher', 'Slasher'),
        ('bicycle', 'Bicycle'),
        ('motorbike', 'Motorbike'),
        ('car', 'Car'),
        ('truck', 'Truck'),
        ('minibus', 'Minibus')
    ],
}

preload_data = PreloadData(
    list_data=list_data)
