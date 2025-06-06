from django.db import models

# Create your models here.
# Criar as classes para fazer os cadastros

# herda de models.Model, herança
class Ingrediente(models.Model):
    # Tipo: CharField
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

# Dirá se é salgado, doce, picante, adstringente, azedo ou amargo 
class SaborDaComida(models.Model):
    nome = models.CharField(max_length=30)
    # Método str, recebe como parâmetro ele mesmo, retorna ele mesmo
    def __str__(self):
        return self.nome
    
class Cardapio(models.Model):

    # Algumas opções, um dicionário com o par chave
    EPOCA = {
        'V' : 'Verão',
        'O' : 'Outono',
        'I' : 'Inverno',
        'P' : 'Primavera',
    }

    # Autofield, ineiro incremental
    codigo = models.AutoField(primary_key=True)
    # verbose_name = legivel para humanos
    nome = models.CharField("nome do prato", max_length=100)
    data_criacao = models.DateField()
    data_ingresso_menu = models.DateField()
    # relacionamento com as chaves estrangeiras
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    saborDaComida = models.ForeignKey(SaborDaComida, on_delete=models.CASCADE, verbose_name="sabor da comida")
    # choices é um novo parâmetro, irá listar as épocas
    epoca = models.CharField("epoca da comida", max_length=2, choices=EPOCA)

    def __str__(self):
        return self.nome
    
    # Depois de criar ou alterar os models, faz a migração. 
    # Antes de fazer a migração efetivamente, verifica se tem migrações: py .\manage.py makemigrations nome_do_app
    # Migração efetiva: py manage migrate
    # Precisa fazer de forma explícita no admin