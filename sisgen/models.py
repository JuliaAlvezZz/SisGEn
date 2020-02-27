from django.db import models
from django.urls import reverse
from datetime import datetime

class Vacina(models.Model):
    tipoVacina = models.CharField(max_length=20, verbose_name='Vacina:')
    descricaoVacina = models.TextField(verbose_name='Descrição:')
    criacaoVacina = models.DateField(default=datetime.now, verbose_name='Data de Registro:')

    def __str__(self):
        return self.tipoVacina

    def get_absolute_url(self):
        return reverse('vacina_edit', kwargs={'pk': self.pk})

class Paciente(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das opções"]
    ]
    nomePaciente = models.CharField(max_length=50, verbose_name='Nome Completo:')
    matriculaPaciente = models.CharField(max_length=20, verbose_name='Matrícula:')
    turmaPaciente = models.CharField(max_length=20, verbose_name='Turma:', blank=True)
    idadePaciente = models.IntegerField(verbose_name='Idade:')
    sexoPaciente = models.CharField(max_length=1, choices=SEXO_CHOICES, default="F", verbose_name='Sexo:')
    telefonePaciente = models.CharField(max_length=20, verbose_name='Telefone do Paciente:')
    telefoneResponsavelPaciente = models.CharField(max_length=20, verbose_name='Telefone do Responsável:', blank=True)

    def __str__(self):
        return self.nomePaciente

    def get_absolute_url(self):
        return reverse('paciente_edit', kwargs={'pk': self.pk})
    
class Procedimento(models.Model):
    nomeProcedimento = models.CharField(max_length=20, verbose_name='Nome do Procedimento:')

    def __str__(self):
        return self.nomeProcedimento

    def get_absolute_url(self):
        return reverse('procedimento_edit', kwargs={'pk': self.pk})

class Atendimento(models.Model):
    paciente = models.ForeignKey("Paciente", on_delete=models.CASCADE, related_name="atendimentos", verbose_name='Paciente:')
    dataHora = models.DateTimeField(default=datetime.now , verbose_name='Data/Hora:')
    procedimento = models.ManyToManyField(Procedimento, verbose_name='Procedimento(s) realizado(s):', blank=True)
    vacinacao = models.ManyToManyField(Vacina, verbose_name='Vacinação do Paciente:', blank=True)
    descricaoAtendimento = models.TextField(verbose_name='Descrição:')

    def __str__(self):
        dh = self.dataHora.strftime("%m/%d/%Y, %H:%M:%S")
        return dh

    def get_absolute_url(self):
        return reverse('atendimento_edit', kwargs={'pk': self.pk})

class Equipamento(models.Model):
    tipoEquipamento = models.CharField(max_length=20, verbose_name='Equipamento:')
    descricaoEquipamento = models.TextField(verbose_name='Descrição:')
    registroEquipamento = models.DateField(default=datetime.now, verbose_name='Data de Registro:')

    def __str__(self):
        return self.tipoEquipamento

    def get_absolute_url(self):
        return reverse('equipamento_edit', kwargs={'pk': self.pk})
