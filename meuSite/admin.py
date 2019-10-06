from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Servico, TipoServico, DestaqueServico, FotoCarousel

admin.site.register(Servico)
admin.site.register(TipoServico)
admin.site.register(DestaqueServico)
admin.site.register(FotoCarousel)


