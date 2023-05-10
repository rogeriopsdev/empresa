# Generated by Django 4.1.7 on 2023-04-01 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_agenda', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id_avaliacao', models.AutoField(db_column='ID_AVALIACAO', primary_key=True, serialize=False)),
                ('nome_avaliacao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=50)),
                ('cnpj_empresa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_servico', models.CharField(max_length=50)),
                ('valor_servico', models.CharField(max_length=50)),
                ('idavaliacao', models.ForeignKey(blank=True, db_column='id_avaliacao', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='empresaapp.avaliacao')),
            ],
        ),
    ]
