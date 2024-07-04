from django.urls import path
from .views import MenuItemsView, SingleMenuItemView, msg, index
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('api/api-token-auth/', obtain_auth_token),
    path('api/menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('api/menu-items/', MenuItemsView.as_view()),
    path('message/', msg),
    path('', index, name='index')
  
]