from django.urls import path
from .views import ListaProfileView, ProfileCreateView

urlpatterns = [
    path('', ListaProfileView.as_view(), name='profile.index'),
    path('novo/', ProfileCreateView.as_view(), name='profile.novo'),
]
