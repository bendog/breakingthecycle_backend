from django.contrib import admin
from .models import Rider, RiderUpdates, Donation
# Register your models here.

admin.site.register(Rider)
admin.site.register(RiderUpdates)
admin.site.register(Donation)