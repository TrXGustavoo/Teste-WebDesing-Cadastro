from django.urls import path
from .views import ListaProfileView, ProfileCreateView, ProfileUpdateView, ProfileDeleteView

urlpatterns = [
    path('', ListaProfileView.as_view(), name='profile.index'),
    path('novo/', ProfileCreateView.as_view(), name='profile.novo'),
    path('edit/<int:pk>', ProfileUpdateView.as_view(), name='profile.edit'),
    path('delete/<int:pk>', ProfileDeleteView.as_view(), name='profile.delete'),
]
