from django.contrib import admin
from senser.models import *


class MeasurementInline(admin.StackedInline):
    model = Measurement
    extra = 3

class SensorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [MeasurementInline]

admin.site.register(Measurement)
admin.site.register(Sensor, SensorAdmin)