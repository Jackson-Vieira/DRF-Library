from rest_framework.serializers import ModelSerializer
from library.models import Aluno, Emprestimo, Livro, Sessao
from rest_framework import serializers

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
            'titulo', 'autor', 'sessao'
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

    def get_data_criacao(self, obj):
        return obj.data_criacao.isoformat()[:10]

    class Meta:
        model = Emprestimo
        fields = (
            'id', 'aluno', 'livro', 'data_criacao', 'situacao'
        )

        extra_kwargs = {
            'data_criacao': {'read_only':True,},
        }