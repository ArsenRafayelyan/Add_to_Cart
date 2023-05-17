from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('cart/',views.cart, name='cart'),
    path('delete_item/',views.delete_item, name='delete_item')


]