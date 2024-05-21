from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('order/', views.order, name="order"),

    path('update_item/', views.updateItem, name="update_item"),
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
]