from django.urls import path, include
from events import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('main', views.Main.as_view(), name='main'),
    path('sign', views.Sign.as_view(), name='sign'),
    path('food', views.Food.as_view(), name='food'),
    path('order', views.Order.as_view(), name='order'),
    path('cater', views.Cater.as_view(), name='cater'),
]
