from rest_framework.serializers import ModelSerializer
from library.models import Aluno, Emprestimo, Livro, Sessao
from rest_framework import serializers

from rest_framework.generics import get_object_or_404

from rest_framework.exceptions import ValidationError

class SessaoSerializer(ModelSerializer):
    class Meta:
        model = Sessao
        fields = (
            'descricao',
            'localizacao',
            'categoria'
        ) #

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = (
            'id', 'titulo', 'autor', 'sessao'
        )
    
class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = (
            'matricula', 'nome'
        )

        extra_kwargs = {
            'email': {'write_only':True,}
        }
        
class EmprestimoSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    data_criacao = serializers.SerializerMethodField()

    aluno_data = serializers.SerializerMethodField()
    livro_data = serializers.SerializerMethodField()

    def get_data_criacao(self, obj):
        return obj.data_criacao.isoformat()[:10]

    def get_aluno_data(self, obj):
        aluno = obj.aluno
        return AlunoSerializer(aluno).data

    def get_livro_data(self, obj):
        livro = obj.livro
        return LivroSerializer(livro).data

    class Meta:
        model = Emprestimo
        fields = '__all__'
        extra_fields = ['aluno_data', 'livro_data']

        extra_kwargs = {
            'data_criacao': {'read_only':True,},
            'aluno_data': {'read_only':True,},
            'livro_data': {'read_only':True,},
        }

    def validate(self, data):
        livro = data.get('livro')
        aluno = data.get('aluno')
        situacao = data.get('situacao')
        try:
            ultimo_emprestimo = Emprestimo.objects.filter(livro=livro)[0]
            
            if ultimo_emprestimo.situacao == 'aberto' and situacao == 'aberto':
                raise ValidationError(f"Este livro não pode ser emprestado, pois sua situação está em {ultimo_emprestimo.situacao}")
        except IndexError:
            pass
        return data