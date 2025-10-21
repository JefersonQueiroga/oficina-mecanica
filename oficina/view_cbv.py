# views.py
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.shortcuts import get_object_or_404, redirect
from .models import Motorista
from .forms import MotoristaForm


class IndexView(TemplateView):
    template_name = "oficina/index.html"
    

class MotoristaListView(ListView):
    model = Motorista
    template_name = "oficina/motorista_list.html"
    context_object_name = "motoristas"


class MotoristaDetailView(DetailView):
    model = Motorista
    template_name = "oficina/motorista_detail.html"
    context_object_name = "motorista"  # mantém alias usado no seu detail


class MotoristaCreateView(CreateView):
    model = Motorista
    form_class = MotoristaForm
    template_name = "oficina/motorista_form.html"
    success_url = reverse_lazy("motorista_list")


class MotoristaUpdateView(UpdateView):
    model = Motorista
    form_class = MotoristaForm
    template_name = "oficina/motorista_form.html"
    success_url = reverse_lazy("motorista_list")


class MotoristaDeleteView(DeleteView):
    model = Motorista
    template_name = "oficina/motorista_confirm_delete.html"
    success_url = reverse_lazy("motorista_list")