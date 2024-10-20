from django.urls import path
from authentication import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/',views.signup,name='signup'),
    # path('login/',views.handlelogin,name='handlelogin'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',views.handlelogout,name='handlelogout'),
]
