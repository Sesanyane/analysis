GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)

RELATIONSHIP = (
    ('father', 'Father'),
    ('mother', 'Mother'),
    ('son', 'Son'),
    ('daughter', 'Daughter'),
    ('grandfather', 'Grandfather'),
    ('grandmother', 'Grandmother'),
    ('uncle', 'Uncle'),
    ('mother_in_law', 'Mother in law'),
    ('father_in_law', 'Father in law'),
    ('son_in_law', 'Son in law'),
    ('daughter_in_law', 'Daughter in law'),
)

ROOF_MATERIAL = (
    ('grass_thatch_hay', 'Grass Thatch/Hay'),
    ('wood', 'Wood'),
    ('iron_sheet', 'Iron sheet'),
    ('cement_concrete', 'Cement/concrete'),
    ('dirt_bricks', 'Dirt bricks'),
    ('plastic_sheeting', 'Plastic sheeting'),
    ('asbestos_sheet', 'Asbestos sheet'),
    ('other', 'Other'),
)

FLOOR_MATERIAL = (
    ('cow_dung', 'Cow dung'),
    ('soil_sand_mud', 'Soil/Sand/Mud'),
    ('wood_planks', 'Wood/Planks'),
    ('palm_bamboo', 'Palm/bamboo'),
    ('cement_concrete', 'Cement/concrete'),
    ('tiles_marble', 'Tiles/Marble'),
    ('other', 'Other'),   
)

WALL_MATERIAL = (
    ('mud_bricks_unburned', 'Mud bricks (unburned)'),
    ('wood', 'Wood'),
    ('sheet_metal', 'Sheet metal'),
    ('rock', 'Rock'),
    ('burned_bricks', 'Burned bricks'),
    ('cement_concrete', 'Cement/concrete'),
    ('straw_thatch', 'Straw/Thatch'),
    ('cardboard', 'Cardboard')
    ('other', 'Other'),
)

SANITARY_FACILITY = (
    ('no_toilet_bush', 'No toilet (bush)'),
    ('latrine', 'Latrine'),
    ('barrel_bucket', 'Barrel/bucket'),
    ('public_toilet', 'Public toilet'),
    ('toilet_in_another_house', 'Toilet in another house'),
    ('sanplat', 'Sanplat'),
    ('other', 'Other'),
)

DRINKING_WATER = (
    ('water_connected_in_house', 'Water connected in house'),
    ('water_boozer_service', 'Water boozer service'),
    ('bottled_water', 'Bottled water'),
    ('public_borehole', 'Public borehole'),
    ('rainwater_spring', 'Rainwater/spring'),
    ('dam_canal', 'Dam/canal'),
)

HOUSE_ARRANGEMENT = (
    ('rent', 'Rent'),
    ('taken_care_of_by_family_friends', 'Taken care of by family/friends'),
    ('living_in_relatives_compound', 'Living in relatives compound'),
    ('other', 'Other, specify'),
)

WASTE_DISPOSAL = (
    ('burning', 'Burning'),
    ('deposit_in_open_pit', 'Deposit in open pit'),
    ('burying_in_close_pit', 'Burying in close pit'),
    ('throw_away_bush_stream', 'Throw away (bush, stream)'),
    ('other', 'Other'),
)

COOKING_ENERGY = (
    ('none_no_kitchen', 'None (no kitchen)'),
    ('fire_wood', 'Fire wood'),
    ('charcoal', 'Charcoal'),
    ('gas_kerosene', 'Gas/kerosene'),
    ('stem_straw', 'Stem/Straw'),
    ('animal_scraps', 'Animal scraps'),
    ('electricity', 'Electricity'),
    ('other', 'Other, specify'),
)

LIGHTING = (
    ('electricity_network', 'Electricity (network)'),
    ('gas_kerosene_lamp', 'Gas/kerosene lamp'),
    ('candle_torch', 'Candle/torch'),
    ('solar_energy', 'Solar energy'),
    ('electricity_generator', 'Electricity generator'),
    ('fueled_light_lamp', 'Fueled light lamp'),
    ('lamp_with_bateries', 'Lamp with batteries'),
    ('no_ligtht', 'No light'),
    ('other', 'Other, specify'),
)

EDUCATION = (
    ('plse', 'PLSE'),
    ('js', 'JC'),
    ('bgcse', 'BGCSE'),
    ('tertiary', 'Tertiary'),
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

YES_NO_NA = (
    ('y', 'Yes'),
    ('n', 'No'),
    ('na', 'N/A')
)


MARITAL_STATUS = (
    ('single', 'Single'),
    ('married', 'Married'),
    ('widowed', 'Widowed'),
    ('divorced', 'Divorced'),
    ('separated', 'Separated')
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

COMMUNITY = (
    ('malwelwe_kweneng', 'Malwelwe, Kweneng District'),
    ('komana_north_west', 'Komana, North West District'),
    ('nxaraga_ngamiland', 'Nxaraga, Ngamiland District'),
    ('werda_kgalagadi_south', 'Werda, Kgalagadi South District'),
    ('maun_ngamiland', 'Maun, Ngamiland District'),
    ('shakawe_north_west', 'Shakawe, North West District'),
    ('kang_kgalagadi_north', 'Kang, Kgalagadi North District'),
    ('bokspits_kgalagadi', 'Bokspits, Kgalagadi District'),
    ('tsetseng_kweneng', 'Tsetseng, Kweneng District'),
    ('gakhibana_kgalagadi_south', 'Gakhibana, Kgalagadi South District'),
    ('maubelo_kgalagadi_south', 'Maubelo, Kgalagadi South District'),
    ('kokotsha_kgalagadi_south', 'Kokotsha, Kgalagadi South District'),
    ('tsabong_kgalagadi_south', 'Tsabong, Kgalagadi South District'),
    ('etsha_6_ngamiland_west', 'Etsha 6, Ngamiland West District'),
    ('tsau_north_west', 'Tsau, North West District'),
    ('kuke_ghanzi', 'Kuke, Ghanzi'),
    ('inalegolo_kgalagadi_north', 'Inalegolo, Kgalagadi north'),
    ('lehututu_kgalagadi_north', 'Lehututu, Kgalagadi north'),
    ('hukuntsi_kgalagadi_north', 'Hukuntsi, Kgalagadi north'),
    ('tshane_kgalagadi_north', 'Tshane, Kgalagadi north'),
    ('diphuduhudu_kweneng', 'Diphuduhudu, Kweneng'),
    ('sorilatholo_kweneng', 'Sorilatholo, Kweneng'),
    ('tshwaane_kweneng', 'Tshwaane Kweneng'),
    ('kaudwane_kweneng', 'Kaudwane Kweneng'),
    ('bere_ghanzi', 'Bere, Ghanzi District'),
    ('ghanzi', 'Ghanzi, Ghanzi District')
)

DISTRICT = (
    ('kweneng', 'Kweneng District'),
    ('kgalagadi_south', 'Kgalagadi South District'),
    ('kgalagadi_north', 'Kgalagadi North District'),
    ('kgalagadi', 'Kgalagadi District'),
    ('ngamiland', 'Ngamiland District'),
    ('north_west', 'North West District'),
    ('ngamiland_west', 'Ngamiland West District'),
    ('ghanzi', 'Ghanzi District'),
    ('kweneng', 'Kweneng District'),
)

HOUSEHOLD_TYPE = (
    ('male_headed', 'Male-headed'),
    ('female_headed', 'Female-headed'),
    ('elderly_male_headed', 'Elderly male-headed'),
    ('elderly_female_headed', 'Elderly female-headed'),
    ('child_headed', 'Child-headed'),
)