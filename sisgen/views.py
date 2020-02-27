from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from sisgen.models import Vacina, Paciente, Atendimento, Equipamento, Procedimento

class IndexTemplateView(TemplateView):
    name="index.html"

class VacinaList(ListView):
    model = Vacina

class VacinaView(DetailView):
    model = Vacina

class VacinaCreate(CreateView):
    model = Vacina
    fields = ['tipoVacina', 'descricaoVacina', 'criacaoVacina']
    success_url = reverse_lazy('vacina_list')

class VacinaUpdate(UpdateView):
    model = Vacina
    fields = ['tipoVacina', 'descricaoVacina', 'criacaoVacina']
    success_url = reverse_lazy('vacina_list')

class VacinaDelete(DeleteView):
    model = Vacina
    success_url = reverse_lazy('vacina_list')

class PacienteList(ListView):
    model = Paciente

class PacienteView(DetailView):
    model = Paciente

class PacienteCreate(CreateView):
    model = Paciente
    fields = ['nomePaciente', 'matriculaPaciente', 'turmaPaciente', 'idadePaciente', 'sexoPaciente', 'telefonePaciente', 'telefoneResponsavelPaciente']
    success_url = reverse_lazy('paciente_list')

class PacienteUpdate(UpdateView):
    model = Paciente
    fields = ['nomePaciente', 'matriculaPaciente', 'turmaPaciente', 'idadePaciente', 'sexoPaciente', 'telefonePaciente', 'telefoneResponsavelPaciente']
    success_url = reverse_lazy('paciente_list')

class PacienteDelete(DeleteView):
    model = Paciente
    success_url = reverse_lazy('paciente_list')

class ProcedimentoList(ListView):
    model = Procedimento

class ProcedimentoView(DetailView):
    model = Procedimento

class ProcedimentoCreate(CreateView):
    model = Procedimento
    fields = ['nomeProcedimento']
    success_url = reverse_lazy('procedimento_list')

class ProcedimentoUpdate(UpdateView):
    model = Procedimento
    fields = ['nomeProcedimento']
    success_url = reverse_lazy('procedimento_list')

class ProcedimentoDelete(DeleteView):
    model = Procedimento
    success_url = reverse_lazy('procedimento_list')

class AtendimentoList(ListView):
    model = Atendimento

class AtendimentoView(DetailView):
    model = Atendimento

class AtendimentoCreate(CreateView):
    model = Atendimento
    fields = ['paciente', 'dataHora', 'procedimento', 'vacinacao', 'descricaoAtendimento']
    success_url = reverse_lazy('atendimento_list')

class AtendimentoUpdate(UpdateView):
    model = Atendimento
    fields = ['paciente', 'dataHora', 'procedimento', 'vacinacao', 'descricaoAtendimento']
    success_url = reverse_lazy('atendimento_list')

class AtendimentoDelete(DeleteView):
    model = Atendimento
    success_url = reverse_lazy('atendimento_list')

class EquipamentoList(ListView):
    model = Equipamento

class EquipamentoView(DetailView):
    model = Equipamento

class EquipamentoCreate(CreateView):
    model = Equipamento
    fields = ['tipoEquipamento', 'descricaoEquipamento', 'registroEquipamento']
    success_url = reverse_lazy('equipamento_list')

class EquipamentoUpdate(UpdateView):
    model = Equipamento
    fields = ['tipoEquipamento', 'descricaoEquipamento', 'registroEquipamento']
    success_url = reverse_lazy('equipamento_list')

class EquipamentoDelete(DeleteView):
    model = Equipamento
    success_url = reverse_lazy('equipamento_list')
