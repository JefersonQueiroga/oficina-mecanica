from django.contrib import admin
from .models import Veiculo, Motorista, Oficina, ServicoManutencao


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
	list_display = ("placa", "modelo")
	search_fields = ("placa", "modelo")
	ordering = ("placa",)
	list_per_page = 20


@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
	list_display = ("nome", "cpf")
	search_fields = ("nome", "cpf")
	ordering = ("nome",)
	list_per_page = 20


@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
	list_display = ("nome",)
	search_fields = ("nome",)
	ordering = ("nome",)
	list_per_page = 20


@admin.register(ServicoManutencao)
class ServicoManutencaoAdmin(admin.ModelAdmin):
	list_display = (
		"veiculo",
		"oficina",
		"motorista",
		"data_servico",
	)
	list_filter = ("data_servico", "oficina")
	search_fields = (
		"veiculo__placa",
		"veiculo__modelo",
		"motorista__nome",
		"descricao",
	)
	autocomplete_fields = ("veiculo", "oficina", "motorista")
	date_hierarchy = "data_servico"
	ordering = ("-data_servico",)
	list_select_related = ("veiculo", "oficina", "motorista")
	list_per_page = 20

