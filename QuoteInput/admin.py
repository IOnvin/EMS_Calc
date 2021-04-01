from django.contrib import admin
from .models import QuoteInputModel, HostingProvider, Location

# Register your models here.


admin.site.register(QuoteInputModel)
admin.site.register(HostingProvider)
admin.site.register(Location)



