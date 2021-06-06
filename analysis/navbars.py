from edc_navbar import NavbarItem, site_navbars, Navbar

analysis = Navbar(name='analysis')

analysis.append_item(
    NavbarItem(
        name='subject',
        label='Subject',
        fa_icon='fa-user-plus',
        url_name='home_url'))

site_navbars.register(analysis)
