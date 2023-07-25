from django.urls import path
from .import views

# define the urls
urlpatterns = [
    path('pengadaan/', views.pengadaan),
    path('pengadaan/<int:pk>/', views.pengadaan_detail),
    path('pengadaan/search/', views.search, name='search'),
]