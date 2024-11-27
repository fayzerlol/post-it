from django.db import models
import json

class Planilha(models.Model):
    arquivo = models.FileField(upload_to='planilhas/')
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Planilha {self.id} - {self.data_upload}"

class SelecaoColunas(models.Model):
    planilha = models.ForeignKey(Planilha, on_delete=models.CASCADE)  # Relaciona com a planilha
    colunas = models.TextField()  # Armazena as colunas selecionadas como texto

    def __str__(self):
        return f"Seleção para {self.planilha}"

class Quadro(models.Model):
    nome = models.CharField(max_length=255)
    colunas_importadas = models.JSONField()  # Armazena as colunas importadas como JSON
    colunas_no_card = models.JSONField()  # Armazena as colunas a serem exibidas nos cards como JSON
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    #Campos de personalização de cores
    coluna_status = models.CharField(max_length=255, null=True, blank=True)  # Coluna de status
    coluna_data = models.CharField(max_length=255, null=True, blank=True)    # Coluna de data

    #Campos de personalização
    tamanho_fonte = models.CharField(max_length=10, default='16px', null=True, blank=True)
    cor_background = models.CharField(max_length=7, default='#ffffff', null=True, blank=True)
    cor_fonte = models.CharField(max_length=7, default='#000000', null=True, blank=True)
    cor_cards = models.CharField(max_length=7, default='#f8f9fa', null=True, blank=True)
    borda_cards = models.CharField(max_length=7, default='#000000', null=True, blank=True)
    sombra_cards = models.CharField(max_length=7, default='0px 0px 10px rgba(0, 0, 0, 0.1)', null=True, blank=True)

    def __str__(self):
        return self.nome

class Card(models.Model):
    quadro = models.ForeignKey(Quadro, on_delete=models.CASCADE, related_name='cards')
    titulo = models.CharField(max_length=100)
    conteudo = models.JSONField()  # Altere para JSONField para facilitar o uso no Django
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    detalhes = models.TextField(blank=True, null=True)  # Mantenha se for necessário para informações adicionais

    def set_conteudo(self, value):
        """Serializa o dicionário Python para JSON e salva no campo `conteudo`."""
        self.conteudo = json.dumps(value)

    def get_conteudo(self):
        """Deserializa o JSON armazenado em `conteudo` para um dicionário Python."""
        return json.loads(self.conteudo)   

    def __str__(self):
        return self.titulo
