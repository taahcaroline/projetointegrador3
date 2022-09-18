from django.shortcuts import render, redirect
from .models import Noticiascad
from .forms import NoticiascadForm
from django.views.generic import ListView

def home(request):
    return render(request, 'busca.html')


#cadastro
def noticiascad(request):
    if request.method == 'POST':
            form = NoticiascadForm(request.POST)
            if form.is_valid():
             noticia = form.save(commit=False)
             noticia.save()

            return redirect('/')
    else:        
        form = NoticiascadForm()
        return render(request, 'cadnoticias.html', {'form': form})


#busca
# class ListaNews(ListView):
#     model = Noticiascad
#     template_name = 'busca.html'
#     def buscar(self):
#       busca = self.GET.get('titulo')
#       if busca:
#         lista = Noticiascad.objects.filter(titulo__icontains = busca)
#       else:

#         lista = Noticiascad.objects.all()
#       return lista

def buscar(request):
    lista = request.GET.get('titulo')
    resultado = Noticiascad.objects.filter(titulo__icontains = lista)
    return render(request, 'resultado.html', {'resultado': resultado})



def noticiascadastradas(request):
    notas = Noticiascad.objects.all()
    
    context = {
        'notas': notas
    }

    return render(request, 'resultado.html',  context)