from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profile
from .forms import ProfileForm


class ListaProfileView(ListView):
    model = Profile
    # dentro da classe de profile pega os objetos e tras todos eles
    queryset = Profile.objects.all().order_by('nome_completo')



class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    success_url = '/pessoas/'


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = '/pessoas/'


class ProfileDeleteView(DeleteView):
    model = Profile
    success_url= '/pessoas/'