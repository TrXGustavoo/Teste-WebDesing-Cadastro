from django.urls import path
from .views import ListaProfileView, ProfileCreateView, ProfileUpdateView, ProfileDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(ListaProfileView.as_view()), name='profile.index'),
    path('novo/',  login_required(ProfileCreateView.as_view()), name='profile.novo'),
    path('edit/<int:pk>', login_required(ProfileUpdateView.as_view()), name='profile.edit'),
    path('delete/<int:pk>', login_required(ProfileDeleteView.as_view()), name='profile.delete'),
]
