from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_page, name='index'),#main page
    path('signup/',views.send_password,name = 'signup'),
    path('login/',views.login_user,name = 'login'),
    path('logout/',views.logout_user,name = 'logout'),
]