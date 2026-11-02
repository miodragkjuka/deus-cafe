from django.contrib import admin

from .models import (ContactMessage, GalleryImage, MenuCategory, MenuItem,
                     Post, Reservation, TeamMember)

admin.site.site_header = 'Деус – администрација'
admin.site.site_title = 'Деус'

admin.site.register(MenuCategory)
admin.site.register(TeamMember)
admin.site.register(Post)
admin.site.register(GalleryImage)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'time', 'guests')
    list_filter = ('date',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created')
