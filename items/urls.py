from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('baazar/', views.baazar),
    path('baazar/<slug:search>', views.baazar),
    path('auctions/', views.auction),
    path('baazar/details/<slug:item_id>/', views.baazar_item),
    path('auctions/<slug:search>/', views.auction),
]