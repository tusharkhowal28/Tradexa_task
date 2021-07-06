from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
    path('',views.signup,name = "signup"),
    path('login/',LoginView.as_view(template_name ='login.html')),
     path('logout/', LogoutView.as_view(template_name='login.html')),
    path('login/home/', views.home,name = "home"),
    path('post/',views.write,name = "post"),
    path('view/',views.view_post,name = "view_post"),
    path('view/<id>/edit/',views.post_edit,name = "edit_post"),
    path('view/<id>/delete/',views.post_delete,name = "delete_post"),

]
