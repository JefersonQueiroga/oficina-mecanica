from django.db import models

class Veiculo(models.Model):
    placa = models.CharField(max_length=7, unique=True)
    modelo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.modelo} ({self.placa})"

class Motorista(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome

class Oficina(models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome

class ServicoManutencao(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, null=True, blank=True, on_delete=models.SET_NULL)
    data_servico = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return f"Serviço em {self.veiculo} - {self.data_servico}"