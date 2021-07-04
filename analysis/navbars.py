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
        name='household',
        label='Household',
        fa_icon='fa-user-plus',
        url_name='household_url'))

site_navbars.register(analysis)
