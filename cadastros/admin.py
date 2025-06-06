from django.contrib import admin

from .models import Ingrediente, SaborDaComida, Cardapio
# Register your models here.

# Registra os models das interfaces que quer gerenciar pelo site
admin.site.register(Ingrediente)
admin.site.register(SaborDaComida)
admin.site.register(Cardapio)
