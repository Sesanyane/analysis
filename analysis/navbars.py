from edc_navbar import NavbarItem, site_navbars, Navbar

analysis = Navbar(name='analysis')

analysis.append_item(
    NavbarItem(
        name='vaccine',
        label='Vaccine Awareness',
        fa_icon='fa-user-plus',
        url_name='vaccine_home_url'))

analysis.append_item(
    NavbarItem(
        name='food_security',
        label='Food Security & Livelihood',
        fa_icon='fa-user-plus',
        url_name='food_security_home_url'))

site_navbars.register(analysis)
