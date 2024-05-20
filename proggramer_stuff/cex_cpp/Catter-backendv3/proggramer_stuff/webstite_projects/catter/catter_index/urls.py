from django.urls import path
from . import views
from .views import update_elo

urlpatterns = [
    path('home/', views.getcats, name='homepage'),  # Define homepage
    path('score/', views.leaderboard, name='leaderboard'),  # Define leaderboard
    path('add_cat/', views.add_cat, name='post_page'),  # Define add_cat page
    path('go/', views.getcats, name='go'),
     path('update_elo/<int:cat_id>/', update_elo, name='update_elo'),
    
]
