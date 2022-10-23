from django.views.generic import ListView
from .models import Livro

class LivrosListView(ListView):
    model = Livro
    queryset = Livro.objects.all()
    template_name = 'library/admin.html'
    
    def get_context_data(self, **kwargs):
        context = {}
        context['livros'] = self.queryset
        return context