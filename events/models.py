from django.db import models


class Event(models.Model):

    priorities_list = (
        ('0','Sem prioridade'),
        ('1','Normal'),
        ('2','Urgente'),
        ('3', 'Muito Urgente'),
        ('4', 't Ultra Mega Hiper Urgente')
    )

    date = models.DateField()
    event = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=priorities_list)

    def __str__(self):
        return self.event

# Create your models here.
