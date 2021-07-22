from django.urls import path,include
from . import views
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth import views as auth_views
from django.urls import path,include

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.registration, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('add-folder', views.add_folder, name="add-folder"),
    path('folder/<folder>', views.folder, name="folder"),
    path('add-card/<folder>', views.add_card, name="add-card"),
    path('delete/<card>',views.delete_card, name="delete"),
    path('edit-card/<card>', views.edit_card, name="edit-card") 

]