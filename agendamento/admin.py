from django.contrib import admin
from .models import Agendamento

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome_paciente', 'data', 'hora', 'medico')
    search_fields = ('nome_paciente', 'medico')
