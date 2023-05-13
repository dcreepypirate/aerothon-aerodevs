from django.urls import path

from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("index", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("market", views.market, name='market'),
    path("buy/<int:part_id>", views.buy, name='buy'),

    path("dashboard", views.dashboard, name='dashboard'),
    path('search', views.search, name="search"),

]