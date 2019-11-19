from django.conf.urls import url
from django.contrib import admin
class CustomAdminSite(admin.AdminSite):
  
    def get_urls(self):
        urls = super(CustomAdminSite, self).get_urls()
        custom_urls = [
            url(r'desired/path$', self.admin_view(organization_admin.preview), name="preview"),
        ]
        return urls + custom_urls
