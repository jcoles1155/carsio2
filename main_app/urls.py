from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/update/<int:pk>/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/delete/<int:pk>/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_comment/', views.add_comment, name='add_comment'),
]