from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profile
from .forms import ProfileForm


class ListaProfileView(ListView):
    model = Profile
    # dentro da classe de profile pega os objetos e tras todos eles
    queryset = Profile.objects.all().order_by('nome_completo')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(usuario=self.request.user)
        filter_nome = self.request.GET.get('nome') or None

        if filter_nome:
            queryset = queryset.filter(nome_completo__contains=filter_nome)
        return queryset
    

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    success_url = '/pessoas/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = '/pessoas/'


class ProfileDeleteView(DeleteView):
    model = Profile
    success_url= '/pessoas/'