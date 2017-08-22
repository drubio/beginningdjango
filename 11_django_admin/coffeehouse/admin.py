from django.contrib.admin import AdminSite

class EmployeeAdminSite(AdminSite):
    site_header = 'Coffeehouse Employee admin'

employeeadmin = EmployeeAdminSite(name='employeeadmin')

class ProviderAdminSite(AdminSite):
    site_header = 'Coffeehouse Provider admin'

provideradmin = ProviderAdminSite(name='provideradmin')
