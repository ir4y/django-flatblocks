from django.contrib import admin
from hvad.admin import TranslatableAdmin
from flatblocks.models import FlatBlock


class FlatBlockAdmin(TranslatableAdmin):
    ordering = ['slug', ]

admin.site.register(FlatBlock, FlatBlockAdmin)
