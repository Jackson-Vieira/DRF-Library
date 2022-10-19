from django.db import models
from django.core.exceptions import ValidationError


CHOICES_CATEGORIA = [
    ('fantasia', 'Fantasia'),
    ('ficção científica', 'Ficção científica'),
    ('distopia', 'Distopia'),
    ('ação e aventura', 'Ação e aventura'),
    ('ficção policial', 'Ficção Policial')
]

CHOICES_SITUACAO = [
    ('aberto','Aberto'),
    ('fechado','Fechado'),
]

"""class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modiefied = models.DateField(auto_now=True)
    class Meta:
        abstract = True
"""

class Sessao(models.Model):
    descricao = models.TextField(max_length=50)
    localizacao = models.CharField(max_length=50)
    category = models.CharField(
        max_length=50,
        choices=CHOICES_CATEGORIA,
    )

    def __str__(self):
        return self.localizacao
    
    class Meta:
        verbose_name = "Sessão"
        verbose_name_plural = "Sessões"
        ordering = ['id',]

class Livro(models.Model):
    titulo = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    autor = models.CharField(max_length=50, blank=True, null=True)
    sessao = models.ForeignKey(Sessao, related_name='livros', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo',]

class Aluno(models.Model):
    matricula = models.CharField(
        max_length=50, 
        primary_key=True, 
        unique=True,
        blank=False,
        null=False)
    nome = models.CharField(max_length=50)
    email= models.EmailField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['nome',]

class Emprestimo(models.Model):
    aluno = models.ForeignKey(Aluno, related_name='emprestimos', on_delete=models.CASCADE, null=False, blank=False)
    livro = models.ForeignKey(Livro, related_name='emprestimo', on_delete=models.CASCADE, null=False, blank=False)
    situacao = models.CharField(max_length=50, choices=CHOICES_SITUACAO, default=CHOICES_SITUACAO[0])
    data_criacao = models.DateTimeField(auto_now_add=True)
    # data_devolução = models.DateField()
    
    class Meta:
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'
        ordering = ['-data_criacao',]
    

    def clean(self):
        try:
            ultimo_emprestimo = Emprestimo.objects.filter(livro=self.livro).latest('id')
            if ultimo_emprestimo.situacao == 'aberto' and ultimo_emprestimo != self:
                raise ValidationError(f"Este livro não pode ser emprestado, pois sua situação está em {self.situacao}")
        except self.DoesNotExist:
            pass
       



        
    
    