from django.contrib import admin
from .models import Aluno, Livro, Sessao, Emprestimo

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
   list_display = ['id','titulo',]

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['matricula','nome',]

@admin.register(Sessao)
class SessaoAdmin(admin.ModelAdmin):
    pass

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ['id','aluno', 'livro', 'data_atualizacao', 'situacao']
    list_filter = ['situacao',]