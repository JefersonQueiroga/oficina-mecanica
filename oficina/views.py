from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib import messages
from .models import Motorista, Veiculo, Oficina, ServicoManutencao
from .forms import MotoristaForm


def index_view(request):
    """View para página inicial com estatísticas"""
    context = {
        'total_veiculos': Veiculo.objects.count(),
        'total_motoristas': Motorista.objects.count(),
        'total_oficinas': Oficina.objects.count(),
        'total_servicos': 0,
    }
    return render(request, "oficina/index.html", context)


def motorista_list_view(request):
    """View para listar motoristas"""
    motoristas = Motorista.objects.all().order_by('nome')
    context = {'motoristas': motoristas}
    return render(request, "oficina/motorista_list.html", context)


def motorista_detail_view(request, pk):
 
    motorista = get_object_or_404(Motorista, pk=pk)
    context = {
        'motorista': motorista,  # Alias para compatibilidade
    }
    return render(request, "oficina/motorista_detail.html", context)


def motorista_create_view(request):
    """View para criar um novo motorista"""
    if request.method == 'POST':
        form = MotoristaForm(request.POST)
        if form.is_valid():
            motorista = form.save()
            return redirect('motorista_list')
    else:
        form = MotoristaForm()
    
    context = {
        'form': form,
    }    
    return render(request, "oficina/motorista_form.html", context)


def motorista_update_view(request, pk):
    """View para atualizar um motorista existente"""
    motorista = get_object_or_404(Motorista, pk=pk)
    
    if request.method == 'POST':
        form = MotoristaForm(request.POST, instance=motorista)
        if form.is_valid():
            motorista = form.save()
            return redirect('motorista_list')
    else:
        form = MotoristaForm(instance=motorista)
    
    context = {
        'form': form,
        'object': motorista,
    }
    return render(request, "oficina/motorista_form.html", context)


def motorista_delete_view(request, pk):
    """View para deletar um motorista diretamente"""
    motorista = get_object_or_404(Motorista, pk=pk)
    nome_motorista = motorista.nome
    motorista.delete()
    return redirect('motorista_list')