from django.db import models

# Formulário de cadastro de noticias
class Noticiascad(models.Model):
    titulo = models.CharField('Titulo da notícia', max_length=200)
    autenticidade = models.BooleanField('Marque se for verdadeira, desmarque se for falsa', default=False)
    linknews = models.URLField('Link', max_length=200, blank=True, null=True)
    

    def __str__(self):
        return self.titulo