from django.urls import path
from . import views

urlpatterns =[
    path('home/',views.getcats,name ='homepage'),#definit homepage
    path('score/',views.leaderboard,name ='leaderboard'),#definit leaderboard
    path('post_page/',views.post_cat,name='post_page'),#definit pagina postare mata)
    path('go/',views.getcats,name = 'go'),
]