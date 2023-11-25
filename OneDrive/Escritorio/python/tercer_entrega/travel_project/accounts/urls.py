from django.contrib import admin
from django.urls import path

from accounts.views import sign_up, login_view, CustomLogoutView, MiPerfilUpdateView,\
    agregar_avatar



urlpatterns = [
    # URLS Usuario y sesion
    path('signup/', sign_up, name="sign_up"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('profile/', MiPerfilUpdateView.as_view(), name="profile"),
    path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
]