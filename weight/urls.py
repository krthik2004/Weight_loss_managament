from django.urls import path
from .views import homepage, signup, user_login, add_weight, weight_history
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', homepage, name='homepage'),  # Homepage
    path('signup/', signup, name='signup'),  # Signup page
    path('login/', user_login, name='login'),  # Login page
    path('weight/add_weight/', add_weight, name='add_weight'),  # Weight adding page
    path('weight_history/', weight_history, name='weight_history'),  # Weight history page
    path('logout/', auth_views.LogoutView.as_view(next_page='homepage'), name='logout'),
]
