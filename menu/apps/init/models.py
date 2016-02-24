from django.db import models

''' ======================MENU========================== '''
class Menu(models.Model):
    # Atributos del Menu
    titulo = models.CharField(max_length=144)

    class Meta:
        verbose_name = ('Menu')
        verbose_name_plural = ('Menus')

    def __unicode__(self):
        return self.titulo
    
''' ==================== FIN MENU======================= '''
