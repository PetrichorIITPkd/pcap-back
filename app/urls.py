from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('api/login/',views.user_login,name="login"),
    path('api/register/', views.signup, name="signup"),
    path('api/logout/',views.user_logout,name="logout"),
    path('api/mt/',views.mailtest ,name="mailtest"),
    path('api/admin/',views.admin_data ,name="admin"),
    path('api/events/apply',views.apply_event ,name="applyEvent"),
    path('api/events/',views.getEventUsers ,name="event"),
    path('api/events/verify',views.verifyCA,name="verifyCA"),
    path('api/verifyTR',views.verifyTR,name="verifyTR"),
    path('api/send_grievance',views.send_grievance,name="send_grievance"),
    path('api/events/unconfirmed',views.getUnconfirmed ,name="unconfirmed"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
]
