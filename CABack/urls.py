from django.urls import path
from . import views

urlpatterns = [
    # path('api/login/',views.user_login,name="login"),
    path('/register/', views.signup, name="signup"),
    # path('api/logout/',views.user_logout,name="logout"),
]
