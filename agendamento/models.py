from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    # Outros campos para o modelo Medico

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    nome_paciente = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True, blank=True)  # Corrigido aqui
    observacoes = models.TextField(max_length=200, default='Sem observações')  # Definido valor padrão

    def __str__(self):
        return f'{self.nome_paciente} - {self.data} {self.hora}'