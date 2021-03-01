from django.contrib import admin

from .models import Organization, OrganizationMember


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address')
    search_fields = ['name', 'phone']


@admin.register(OrganizationMember)
class OrganizationMemberAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'user', 'phone', 'organization', 'birthdate')
    search_fields = ['name', 'phone']
