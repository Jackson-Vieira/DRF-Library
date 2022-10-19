from .views import  SessaoViewSet, LivroViewSet, AlunoViewSet, EmprestimoViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'sessoes', SessaoViewSet)
router.register(r'livros', LivroViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'emprestimos', EmprestimoViewSet)