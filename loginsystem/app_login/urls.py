from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboards/', views.dashboards, name='dashboards'),
    path('logout/', views.user_logout, name='logout'),
    path('sentence_importance/', views.sentence_importance, name='sentence_importance'),

]