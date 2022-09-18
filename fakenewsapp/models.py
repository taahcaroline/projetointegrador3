from django.db import models

# Formulário de cadastro de noticias
class Noticiascad(models.Model):
    titulo = models.CharField('Titulo da notícia', max_length=200)
    autenticidade = models.CharField('Verdadeiro ou Falso?', max_length=10)
    linknews = models.URLField('Link', max_length=200)
    

    def __str__(self):
        return self.titulo