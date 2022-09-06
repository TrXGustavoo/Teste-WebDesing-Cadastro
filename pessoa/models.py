from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    nome_completo = models.CharField(max_length=256)
    intolerancia_a_Gluten = models.BooleanField(default=False)
    intolerancia_a_Lactose = models.BooleanField(default=False)
    # data_nascimento = models.DateTimeField(null=True)
    idade = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.nome_completo