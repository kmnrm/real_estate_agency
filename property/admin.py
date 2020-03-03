from django.contrib import admin

from .models import Flat, Complaint

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address')
    readonly_fields = ['created_at']
    list_display = ('town', 'address', 'price', 'new_building', 'construction_year',)
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'complainant',)

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)