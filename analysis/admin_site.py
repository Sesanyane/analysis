from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_url = '/administration/'
    enable_nav_sidebar = False
    site_header = 'Analysis'
    site_title = 'Analysis'
    index_title = 'Analysis'


analysis_admin = AdminSite(name='analysis_admin')
