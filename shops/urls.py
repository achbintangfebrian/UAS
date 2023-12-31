from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='shops.index'),
    path('add', views.add, name='shops.add'),
    path('save', views.save, name='shops.save'),
    path('edit/<int:buy_id>/', views.edit, name='shops.edit' ),
    path('update,/<int:buy_id>/', views.update, name='shops.update' ),
    path('delete,/<int:buy_id>/', views.delete, name='shops.delete' ),

]