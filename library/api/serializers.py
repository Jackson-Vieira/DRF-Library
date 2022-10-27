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
    
    aluno = AlunoSerializer(read_only=True)
    aluno_id = serializers.CharField(write_only=True)
   
    livro = LivroSerializer(read_only=True)
    livro_id = serializers.IntegerField(write_only=True)


    class Meta:
        model = Emprestimo
        fields = (
            'id', 'livro_id', 'aluno_id', 'situacao', 'aluno', 'livro', 'data_criacao', 'data_atualizacao'
        )

        extra_kwargs = {
            'data_criacao': {'read_only':True,},
        }


    def validate(self, data):
        method = self.context['request'].method
        livro_id = data.get('livro_id')
        livro_situacao = data.get('situacao')

        try:
            if Emprestimo.objects.filter(livro_id=livro_id, situacao='aberto').exists() and (method != "PUT" or livro_situacao == "aberto"):
                raise ValidationError(f"Este livro não pode ser emprestado, pois sua situação está em ABERTA!")
        except IndexError:
            pass

        return data

    def create(self, validated_data):
        return Emprestimo.objects.create(**validated_data)