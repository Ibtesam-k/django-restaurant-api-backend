from django.urls import path
from .views import MenuItemsView, SingleMenuItemView
urlpatterns = [
    #path('menu/',MenuView.as_view()),
    path('items/', MenuItemsView.as_view()),
    path('items/<int:pk>', SingleMenuItemView.as_view()),
   
]