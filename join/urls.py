from . import views
from django.urls import path
urlpatterns = [
    path('join/register/',views.register,name='register'),
    path('join/login/',views.login,name='login'),
    path('join/Logout/',views.Logout,name='Logout'),

]