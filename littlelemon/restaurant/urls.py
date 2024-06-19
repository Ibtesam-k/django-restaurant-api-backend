from django.urls import path
from .views import MenuItemsView, SingleMenuItemView, msg
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    #path('menu/',MenuView.as_view()),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('message/', msg),
    path('api-token-auth/', obtain_auth_token),
  
]