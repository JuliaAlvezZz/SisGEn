from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views
from sisgen.views import IndexTemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="sisgen/index.html"), name='index'),
    path('vacinas', views.VacinaList.as_view(), name='vacina_list'),
    path('visualizar-vacina/<int:pk>', views.VacinaView.as_view(), name='vacina_view'),
    path('nova-vacina', views.VacinaCreate.as_view(), name='vacina_new'),
    path('editar-vacina/<int:pk>', views.VacinaUpdate.as_view(), name='vacina_edit'),
    path('deletar-vacina/<int:pk>', views.VacinaDelete.as_view(), name='vacina_delete'),
    path('pacientes', views.PacienteList.as_view(), name='paciente_list'),
    path('visualizar-paciente/<int:pk>', views.PacienteView.as_view(), name='paciente_view'),
    path('novo-paciente', views.PacienteCreate.as_view(), name='paciente_new'),
    path('editar-paciente/<int:pk>', views.PacienteUpdate.as_view(), name='paciente_edit'),
    path('deletar-paciente/<int:pk>', views.PacienteDelete.as_view(), name='paciente_delete'),
    path('atendimentos', views.AtendimentoList.as_view(), name='atendimento_list'),
    path('visualizar-atendimento/<int:pk>', views.AtendimentoView.as_view(), name='atendimento_view'),
    path('novo-atendimento', views.AtendimentoCreate.as_view(), name='atendimento_new'),
    path('editar-atendimento/<int:pk>', views.AtendimentoUpdate.as_view(), name='atendimento_edit'),
    path('deletar-atendimento/<int:pk>', views.AtendimentoDelete.as_view(), name='atendimento_delete'),
    path('equipamentos', views.EquipamentoList.as_view(), name='equipamento_list'),
    path('visualizar-equipamento/<int:pk>', views.EquipamentoView.as_view(), name='equipamento_view'),
    path('novo-equipamento', views.EquipamentoCreate.as_view(), name='equipamento_new'),
    path('editar-equipamento/<int:pk>', views.EquipamentoUpdate.as_view(), name='equipamento_edit'),
    path('deletar-equipamento/<int:pk>', views.EquipamentoDelete.as_view(), name='equipamento_delete'),
    path('procedimentos', views.ProcedimentoList.as_view(), name='procedimento_list'),
    path('visualizar-procedimento/<int:pk>', views.ProcedimentoView.as_view(), name='procedimento_view'),
    path('novo-procedimento', views.ProcedimentoCreate.as_view(), name='procedimento_new'),
    path('editar-procedimento/<int:pk>', views.ProcedimentoUpdate.as_view(), name='procedimento_edit'),
    path('deletar-procedimento/<int:pk>', views.ProcedimentoDelete.as_view(), name='procedimento_delete'),
    path('alterar-senha', auth_views.PasswordChangeView.as_view(template_name='registration/senha.html', extra_context={'titulo': 'Alterar senha atual'}, success_url=reverse_lazy('index')), name='alterar-senha'),
]
