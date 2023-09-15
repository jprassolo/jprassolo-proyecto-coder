from django.contrib import admin
from appPortfolioTracker.models import Portfolio, Activos, Crypto, Bonos, Libro

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Activos)
admin.site.register(Crypto)
admin.site.register(Bonos)
admin.site.register(Libro)
