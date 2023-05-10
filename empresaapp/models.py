from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome_empresa = models.CharField(max_length=50)
    cnpj_empresa= models.CharField(max_length=50)

    def __str__(self):
        return self.nome_empresa

class Avaliacao(models.Model):
    id_avaliacao = models.AutoField(db_column='ID_AVALIACAO' ,primary_key=True)
    nome_avaliacao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_avaliacao


class Status(models.Model):
    nome_status =models.CharField(max_length=50)

    def __str__(self):
        return self.nome_status


class Agenda(models.Model):
    data_agenda = models.CharField(max_length=20)

    def __str__(self):
        return self.data_agenda


class Servico(models.Model):
    nome_servico = models.CharField(max_length=50)
    valor_servico = models.CharField(max_length=50)
    idavaliacao = models.ForeignKey(Avaliacao,models.DO_NOTHING, db_column='id_avaliacao', blank=True, null=True)

    def __str__(self):
        return self.nome_servico
