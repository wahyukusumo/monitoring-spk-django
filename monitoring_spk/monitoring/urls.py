from django.urls import path
from .import views

# define the urls
urlpatterns = [
    path('pengadaan/', views.pengadaan),
    path('pengadaan/<int:pk>/', views.pengadaan_detail),
    path('pengadaan/search/', views.search, name='search'),
    path('keuangan/', views.keuangan),
    path('pengawasan/', views.pengawasan),
]