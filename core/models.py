from django.db import models

class TB_CATEGORIAS(models.Model):
    NOME = models.CharField('NOME', max_length=50)

class TB_PROJETOS(models.Model):
    TITULO = models.CharField('TITULO', max_length=100)
    DESCRICAO = models.TextField('DESCRICAO')
    CATEGORIA = models.ForeignKey(TB_CATEGORIAS, on_delete=models.PROTECT)

class TB_ALUNO(models.Model):
    MATRICULA = models.CharField('MATRICULA', max_length=14, primary_key=True)
    NOME = models.TextField('MATRICULA')
    EMAIL = models.TextField('EMAIL')
    PROJETO = models.ForeignKey(TB_PROJETOS, on_delete=models.PROTECT)







