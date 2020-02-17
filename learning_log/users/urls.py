from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from .import views

app_name ="users"
urlpatterns = [
#登录界面
path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
path('logout/',LogoutView.as_view(), name='logout'),
path('register',views.register,name='register')
]