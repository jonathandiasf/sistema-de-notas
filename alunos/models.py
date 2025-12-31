from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    nota1 = models.FloatField()
    nota2 = models.FloatField()
    nota3 = models.FloatField()

    @property
    def media(self):
        """Média aritmética das três notas, arredondada para 2 casas."""
        return round((self.nota1 + self.nota2 + self.nota3) / 3, 2)

    @property
    def situacao(self):
        return "Aprovado" if self.media >= 7 else "Reprovado"

    def __str__(self):
        return self.nome
