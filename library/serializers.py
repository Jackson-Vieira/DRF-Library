from rest_framework.serializers import ModelSerializer
from library.models import Aluno, Emprestimo, Livro, Sessao

class SessaoSerializer(ModelSerializer):
    class Meta:
        model = Sessao
        fields = '__all__'

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
    
class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

        extra_kwargs = {
            'email': {'write_only':True,}
        }
        
class EmprestimoSerializer(ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'
        extra_kwargs = {
            'data_criacao': {'read_only':True,},
            'situacao': {'read_only':True,}
        }