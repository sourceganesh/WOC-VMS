from django.urls import path,include
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('register', views.registration_view, name="register"),
    path('login', views.login_view, name="login"),
    path('authenticate', views.must_authenticate_view, name="must_auth"),
]