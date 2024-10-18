from django.urls import path

from . import views

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("signup/", views.user_signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path('quests/day/<int:day>/', views.quest_list, name='quest_list'),
    path('quests/<int:quest_id>/', views.quest_detail, name='quest_detail'),
]