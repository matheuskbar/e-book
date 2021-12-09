from django.db import models

class Ebook(models.Model):
    titulo = models.CharField('Título', max_length=100)
    autor = models.CharField('Autor', max_length=100)
    capitulo = models.CharField('Capitulo', max_length=100)
    conteudo = models.TextField('Conteudo', blank=False)