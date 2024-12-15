from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'main/login.html'), name='login'),
    path('register/' , views.register_view , name = 'signup'),
    path('' , views.main , name = 'main'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('results' , views.results , name = 'results')

]
