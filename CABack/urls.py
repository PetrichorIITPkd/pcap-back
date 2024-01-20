from django.urls import path
from . import views

urlpatterns = [
    path('/login/',views.login,name="login"),
    path('/register/', views.signup, name="signup"),
    # path('api/logout/',views.user_logout,name="logout"),
]
