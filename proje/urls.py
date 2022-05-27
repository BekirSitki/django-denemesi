from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ekle/', views.ekle, name='ekle'),
    path('ekle/notekle', views.notekle, name='notekle'),
    path('sil/<int:id>', views.sil, name='sil'),
    path('duzenle/<int:id>', views.duzenle, name='duzenle'),
    path('duzenle/notuduzenle/<int:id>', views.notuduzenle, name='notuduzenle'),
]