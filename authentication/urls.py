
from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserAuthView.as_view(),name='user_auth'),
    path('signup/', views.UserCreateView.as_view(),name='sign_up')
]