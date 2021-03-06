# Generated by Django 2.2.3 on 2019-11-14 03:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sisgen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='dataHora',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data/Hora:'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='descricaoAtendimento',
            field=models.TextField(verbose_name='Descrição:'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atendimentos', to='sisgen.Paciente', verbose_name='Paciente:'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='vacinacao',
            field=models.ManyToManyField(to='sisgen.Vacina', verbose_name='Vacinação do Paciente:'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='descricaoEquipamento',
            field=models.TextField(verbose_name='Descrição:'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='registroEquipamento',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de Registro:'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='tipoEquipamento',
            field=models.CharField(max_length=20, verbose_name='Equipamento:'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='idadePaciente',
            field=models.IntegerField(verbose_name='Idade:'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='matriculaPaciente',
            field=models.CharField(max_length=20, verbose_name='Matrícula:'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nomePaciente',
            field=models.CharField(max_length=50, verbose_name='Nome Completo:'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexoPaciente',
            field=models.CharField(choices=[['F', 'Feminino'], ['M', 'Masculino'], ['N', 'Nenhuma das opções']], default='F', max_length=1, verbose_name='Sexo:'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefonePaciente',
            field=models.CharField(max_length=20, verbose_name='Telefone do Paciente:'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefoneResponsavelPaciente',
            field=models.CharField(max_length=20, verbose_name='Telefone do Responsável:'),
        ),
        migrations.AlterField(
            model_name='procedimento',
            name='nomeProcedimento',
            field=models.CharField(max_length=20, verbose_name='Nome do Procedimento:'),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='criacaoVacina',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de Registro:'),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='descricaoVacina',
            field=models.TextField(verbose_name='Descrição:'),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='tipoVacina',
            field=models.CharField(max_length=20, verbose_name='Vacina:'),
        ),
    ]
